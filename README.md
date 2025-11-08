# Тестовое задание: Приложение с кеширующим слоем

## Компоненты
- **bubuntu1 (192.168.56.10)**: PostgreSQL 15 + Go Backend (.deb)
- **bubuntu2 (192.168.56.11)**: Redis 7 + Flask Proxy в контейнере CentOS (.rpm)

## Архитектура
Внешний запрос → Proxy (Flask) → Redis (кеширование) → Backend (Go) → PostgreSQL

## Соответствие ТЗ
✅ .deb и .rpm пакеты собраны  
✅ Сервисы управляются через systemctl / контейнер  
✅ Кеширование работает: `cached: false` → `cached: true`  
✅ Сетевая изоляция через iptables  
✅ Прокси доступен извне, backend и PostgreSQL — только по правилам

## Скриншоты смотри в файле pdf
