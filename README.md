# Тестовое задание для команды Телеком
### Скрипт на Python (script/http_requests.py) выполняет HTTP-запросы к нужным адресам и логирует результат в консоль.

Небольшое уточнение: для статус-кодов 1хх тело будет ответа будет пустым

### Dockerfile (docker/Dockerfile) собирает минимальный образ на базе Ubuntu, устанавливает Python и необходимые зависимости, а также копирует внутрь контейнера наш скрипт. При запуске контейнера скрипт автоматически выполняется.

Запуск Dockerfile из корневой папки:

docker build -f docker/Dockerfile .

### Ansible
/ansible/docker_install.yml — добавляет необходимые репозитории, устанавливает сам Docker, настраивает пользователя (добавляет его в группу docker для работы без sudo) и запускает сервис. 

/ansible/container_playbook.yml - автоматизирует сборку и запускает контейнер с Python-скриптом. Сначала он копирует Dockerfile и сам скрипт на сервер, затем собирает Docker-образ, запускает контейнер, дожидается завершения работы скрипта, проверяет код возврата и выводит логи.

Запуск плейбуков из корневой папки:
  ansible-playbook -i ansible/hosts.ini ansible/docker_install.yml  
  ansible-playbook -i ansible/hosts.ini ansible/container_playbook.yml

## Контакт для связи
telegram @tweezyx
