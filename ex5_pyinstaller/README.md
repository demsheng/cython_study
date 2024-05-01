## ex5  演示pyinstaller打包动态链接库

- 2024-05-01
- 李长圣

### 安装pyinstaller

```
pip install pyinstaller
pip install tinyaes # 用于--key mypassword 设置密码，防止反编译
```

### 打包成 exe 

- 情况1：动态链接库 `.so` 在当前目录
    ```
    #--key设置密码，防止反编译
    pyinstaller --key 12345 -F test.py 
    ```
- 情况2：动态链接库 `.so` 不在当前目录
    ```
    # 生成配置文件
    pyi-makespec --key 123456 -F test.py
    # 在配置文件中，添加动态链接库路径
    # binaries=[("/home/lichangsheng/Desktop/cython_study/ex4_staticlib/build/lib.linux-x86_64-3.6/wrapper_staticlib.cpython-36m-x86_64-linux-gnu.so",".")],
    # 打包
    pyinstaller -F test.py
    ```

### 运行
```
python ./dist/test
```

### 参考 https://www.jianshu.com/p/e684c17ee91c