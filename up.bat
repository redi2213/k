@echo off
cd /d %~dp0

echo ------------------------------
echo افزودن همه فایل‌ها به استیج...
git add .

echo ------------------------------
set /p msg=پیام کامیت را وارد کنید: 

git commit -m "%msg%"

echo ------------------------------
echo در حال پوش کردن به GitHub...
git push origin main

echo ------------------------------
echo ✅ همه چیز انجام شد.
pause
