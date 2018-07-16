from distutils.core import setup

setup(name="message_whx",
      version="1.0",
      description="whx 消息发送和接收",
      long_description="完整的发送和接收消息模块",
      author="whx",
      author_email="434745765@qq.com",
      url="mlweihx.github.com",
      py_modules=["message_whx.send_message",
                  "message_whx.receive_message"])