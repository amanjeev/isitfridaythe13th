import datetime

now = datetime.datetime.now()

print 'Content-Type: text/html'
print ''
print '<!DOCTYPE html><html lang ="en"><head></head><body style="text-align: center; padding-top: 200px;"><div class="content" style="font-weight: bold; font-size: 220px; font-family: Arial,sans-serif; text-decoration: none; color: black;">'

if now.weekday() == 4 and now.day == 13:
    print 'YES'
else:
    print 'NO'

print '</div></body></html>'
