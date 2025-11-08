Name: proxy
Version: 1.0
Release: 1%{?dist}
Summary: Flask proxy with Redis caching
License: MIT
URL: https://example.com

Requires: python3-flask python3-redis python3-requests redis

%description
Flask-based proxy that caches responses from backend in Redis.

%install
mkdir -p %{buildroot}/opt/proxy
cp -r app/* %{buildroot}/opt/proxy/

%files
/opt/proxy/

%changelog
* Sat Nov 08 2025 Talpa <talpa@example.com> - 1.0-1
- Initial package
