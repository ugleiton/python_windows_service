1. Requisitos

    pip install pywin32

2. Verificar DLL do Python
    * Na pasta de instalação do python "..\Lib\site-packages\win32" deve ter uma DLL com nome: "pywintypes37.dll" no meu caso é a "pywintypes37" pois estou usando o python 3.7, este número irá variar de acordo com sua versão;
    * Caso a DLL não esteja na pasta citada acima verifique na seguinte pasta "..\Lib\site-packages\pywin32_system32", procure a DLL e faça uma cópia para a pasta         "..\Lib\site-packages\win32";

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

6. Controle
```   
net start MyServicePython
net stop MyServicePython
```



Referencias:

- https://thepythoncorner.com/posts/2018-08-01-how-to-create-a-windows-service-in-python/
- https://github.com/eduardofaneli/PythonWinService
- https://github.com/SublimeText/Pywin32/blob/master/lib/x32/win32/lib/win32serviceutil.py
