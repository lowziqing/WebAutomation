import datetime


class TimeManager:

    def getDateTime(self):
        now = datetime.datetime.now()
        currentDateTime = now.strftime("%Y-%m-%d %H:%M")
        currentTime = now.strftime("%H%M")
        currentDay = now.strftime("%A")
        return {'currentDateTime': currentDateTime, 'currentTime': currentTime, 'currentDay': currentDay}

    def checkDays(self, days):
        websites = {
            'Monday': "https://www.youtube.com/watch?v=WS93LMcRGRk",
            'Tuesday': "https://www.youtube.com/watch?v=WS93LMcRGRk",
            'Wednesday': "https://www.youtube.com/watch?v=WS93LMcRGRk",
            'Thursday': "https://www.youtube.com/watch?v=SGlkwKA-t_4",
            'Friday': "https://www.youtube.com/watch?v=gS9o1FAszdk",
            'Saturday': "https://www.youtube.com/watch?v=WS93LMcRGRk",
            'Sunday': "https://www.youtube.com/watch?v=WS93LMcRGRk"
        }
        return websites.get(days)


TM = TimeManager()
print(TM.checkDays("Monday"))


