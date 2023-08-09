# akari_motion_server

AKARIのヘッドを動かして感情表現をするモーションサーバアプリ

## 仮想環境の作成
`python -m venv venv`  
`source venv/bin/activate`  
`pip install -r requirements.txt`  

## サーバの起動
`python3 server.py`  

## サンプルアプリの実行
- 実行方法のサンプル  
`python3 simple_client_example.py`  

- M5のボタンで操作するサンプル  
`python3 m5_client_example.py`  

## 使い方

```python
motion_server_port = "localhost:50055"
channel = grpc.insecure_channel(motion_server_port)
stub = motion_server_pb2_grpc.MotionServerServiceStub(channel)

#モーション"bow"をセット
reply = stub.SetMotion(motion_server_pb2.SetMotionRequest(name="bow", priority=3 repeat=True, clear=True))
#セットされているモーションをクリア
reply = stub.ClearMotion(motion_server_pb2.ClearMotionRequest())
#2秒待機
reply = stub.SetWait(motion_server_pb2.SetWaitRequest(time=2.0, priority=3))
```

## priority, repeat, clearについて
・priority:int SetMotionする時にpriorityの値をセットすると、モーション実行中にその値以下のpriorityでSetMotionしようとした場合にブロックする。省略可能。デフォルトは0  
・repeat:bool 次のSetMotionもしくはClearMotionが実行されるまでモーションを繰り返す。省略可能。デフォルトはFalse  
・clear:bool Trueの場合、既にセットされているモーションを全て削除して、新たにモーションをセットする。省略可能。デフォルトはFalse  

## モーション一覧
下記のモーション名を呼び出し可能  
- nod: うなずく  
- agree: 同意する  
- bow: お辞儀する  
- swing: 首を振る  
- happy: 喜ぶ  
- lough: 笑う  
- depressed: 落ち込む  
- amazed: うんざりする  
- sleep: 眠る  
- lookup: 見上げる  
