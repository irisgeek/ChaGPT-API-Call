from config.chatgpt_config import config_dict
from src.openai_request import OpenAI_Request
from tools.cfg_wrapper import load_config

from tools.cfg_wrapper import load_config
from tools.context import ContextHandler
from tools.tokennizer import Tokennizer

import time
import os
import datetime

log_folder = './chatGPTlogs'


class python_api_handler(object):

    def __init__(self,context_max=3200):
        super().__init__()

        # load config
        config = load_config(config_dict)
        keys = config.Acess_config.authorization
        model_name = config.Model_config.model_name
        request_address = config.Model_config.request_address

        # load context
        context_manage_config = config.Context_manage_config
        del_config = context_manage_config.del_config
        max_context = context_manage_config.max_context
        self.context_handler = ContextHandler(max_context=max_context, context_del_config=del_config)
        self.context_max = context_max

        # load tokenizer
        self.tokenizer = Tokennizer(model_name)

        # for test
        self.requestor = OpenAI_Request(keys, model_name,request_address)

    def generate_massage(self,user_input):
        date_today = datetime.datetime.now().strftime("%Y-%m-%d")

        # 获取当前日期 #确保日志文件夹存在，如果不存在则创建一个
        if not os.path.exists(log_folder):
            os.makedirs(log_folder) #新建日志文件，文件名为当前日期 
        log_file_path = os.path.join(log_folder, f'log_{date_today}.txt')
        
        #写入日志到文件中
       

        if user_input == "clear":
            self.context_handler.clear()
            print('start a new session')
            with open(log_file_path, 'a') as f:
                f.write('start a new session\n')
        else:
            inputs_length = self.tokenizer.num_tokens_from_string(user_input)
            self.context_handler.append_cur_to_context(user_input,inputs_length)
            print(f'question:{user_input}')
            with open(log_file_path, 'a') as f:
                f.write(f'question:{user_input}\n')

        st_time = time.time()

        res = self.requestor.post_request(self.context_handler.context)
        ed_time = time.time()

        print(f'post request time cost = {ed_time - st_time}')


        with open(log_file_path, 'a') as f:

            f.write(f'post request time cost = {ed_time - st_time}\n')

        if res.status_code == 200:
          
            print(res.json())
           
            response = res.json()['choices'][0]['message']['content']
            # cut \n for show
            response = response.lstrip("\n")

            completion_length = res.json()['usage']['completion_tokens']
            total_length = res.json()['usage']['total_tokens']
           
            print(f"\nresponse : {response}")
            
            self.context_handler.append_cur_to_context(response,completion_length,tag=1)
            if total_length > self.context_max:
                self.context_handler.cut_context(total_length,self.tokenizer)

            print(f'append context time cost = {time.time() - ed_time}')
            with open(log_file_path, 'a') as f:
                f.write(f"\nresponse : {response}\n")
            return response
        else:
            with open(log_file_path, 'a') as f:
                f.write(res.json()+'\n')
            return '!!! The api call is abnormal, please check the backend log'





