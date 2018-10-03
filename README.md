MD5-hash-light
============
Веб-сервис, позволяющий посчитать MD5-хеш от файла, расположенного в интернете

Установка
============
Используя систему управления пакетами pip устанавливаем необходимые модули.
============
Пример использования сервиса:

>>> curl -X POST -d
"email=user@example.com&url=http://site.com/file.txt"
http://localhost:8000/submit
{"id":"0e4fac17-f367-4807-8c28-8a059a2f82ac"}

>>> curl -X GET http://localhost:8000/check?id=0e4fac17-f367-
4807-8c28-8a059a2f82ac
{"status":"running"}

>>> curl -X GET http://localhost:8000/check?id=0e4fac17-f367-
4807-8c28-8a059a2f82ac
{"md5":"f4afe93ad799484b1d512cc20e93efd1","status":"done","url":"
http://site.com/file.txt"}
