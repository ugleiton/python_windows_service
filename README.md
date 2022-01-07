1. Instalar virtualenv windows
```
python -mvenv venv
venv\Scripts\activate.bat
pip install pywin32
```

2. Verificar DLL do Python
   
    - Certifique-se de ter o arquivo pywintypes37.dll no diretorio: *venv\Lib\site-packages\win32* ("37" é a versão da sua instalação Python). 
    - Se o diretorio não tem esse arquivo pegue-o de: *venv\Lib\site-packages\pywin32_system32\pywintypes37.dll* e cole em *venv\Lib\site-packages\win32*

3. Instalação 
```
python my_service_windows.py install
```

4. Remoção 
```
python my_service_windows.py remove
```

5. Atualização
```
python my_service_windows.py update
```

6. Controle do serviço
```   
net start MyServicePython
net stop MyServicePython
```

7. Debug
```
python my_service_windows.py debug
```



Referencias:

- https://thepythoncorner.com/posts/2018-08-01-how-to-create-a-windows-service-in-python/
- https://github.com/eduardofaneli/PythonWinService
- https://github.com/SublimeText/Pywin32/blob/master/lib/x32/win32/lib/win32serviceutil.py
- https://stackoverflow.com/a/70625723/9930021
