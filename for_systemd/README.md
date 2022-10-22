Файлы *.service и *.timer нужно закинуть в /etc/systemd/system

Затем выполнить: sudo systemctl daemon-reload (чтобы systemd увидел обновленные/новые юниты)

Затем все сервисы запустить:
 - sudo systemctl enable --now my-web-db.service
 - sudo systemctl enable --now my-web-db-backup.service
 - sudo systemctl enable --now my-web-db-backup.timer
Потом можно перезапускать и тд (если где-то накосячили): sudo systemctl status/start/restart <service>


После чего будет запущено приложение, которое поднимается если его насильно прибить или если оно упадет само.

Также заупускается скрипт бэкапа каждую минуту.