# ChaGPT-API-Call

## overall
This project uses python to simply implement the experience of how to call Chagpt's api for dialogue and other tasks.

## how to run
1. install python package(terminal):
    - install openai api(optional): "pip install openai";
    - install tiktoken to calculate the length of tokens: "pip install tiktoken" ,if tips "time out",please add the local sources,such as "pip install tiktoken --      timeout=300 -i https://pypi.tuna.tsinghua.edu.cn/simple";
2. if you want to show conversation on your web, you can install flask use this conmmand: "pip install -r requirements.txt"
3. Add your openAI key to the "authorization" in the config/chatgpt_config.py;
4. Two method you can choose:
    - show in terminal:run this command "python test.py" in your terminal,or run test.py in your ide.
    - show in your local web:
        -   run this command "python manager.py"
        -   run html use ide,click the browser button 
![image](https://user-images.githubusercontent.com/17317538/232182041-2c7db788-b5fa-4d92-a4a7-e381a8da4276.png)


## notice
- You can also use the OpenAI api (https://platform.openai.com/docs/guides/chat) to call, but it’s more flexible and convenient to implement by yourself to expand more applicatioins.
  
  ![image](https://user-images.githubusercontent.com/17317538/222936144-e1b52aa2-b400-4680-a2cb-7dd7ffd99a93.png)
- The dialogue is entered directly from the command line. By default, the context of the dialogue will always be accumulated. If you want to clear the context, you can directly enter 'clear' on the command line.
- The recently added method of deleting the history dialogue is implemented in tools/utils.py. At present, I think there is still a lot of room for optimization in this method. I try to adjust the parameters, this set of default parameters in config.py is relatively optimal in my attempt, you can also configure it in this file.


## features
- support mutil-turn dialogue
- support delete the former dialogue automatically when the token length exceeds the limit of OpenAI API
- support show conversation on local web

## dialogue show
- multi turn
![image](https://user-images.githubusercontent.com/17317538/222916920-4bf3a9bc-68de-4e3d-86b4-12881c5c6926.png)

- Preserve context ability after deleting several dialogues in round 45
![image](https://user-images.githubusercontent.com/17317538/224521387-cbc3db6b-8638-4ece-bfc5-dbf6dd1d9bdb.png)

- local web show the conversation
![image](https://user-images.githubusercontent.com/17317538/232182087-cb2cd336-d150-4d44-be33-ce95d4231d2d.png)


