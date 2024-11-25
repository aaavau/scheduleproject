import calendar
from datetime import date
from django.utils.html import format_html

class ScheduleCalendar(calendar.HTMLCalendar):
    def __init__(self, schedules):
        super().__init__()
        self.schedules = schedules  # スケジュールデータを保持

    def formatday(self, day, weekday, year, month):
        """指定された日付のHTMLを生成"""
        if day == 0:
            # 月の範囲外の日付
            return '<td class="noday bg-light">&nbsp;</td>'
        else:
            day_date = date(year, month, day)
            events = self.schedules.get(day_date, [])
            # イベント情報をBootstrapのbadgeで表示
            events_html = "".join(
                format_html('<div class="badge bg-primary mb-1">{}</div>', event.title)
                for event in events
            )
            return format_html(
                '<td class="day border p-2"><span class="date fw-bold">{}</span><div class="events mt-1">{}</div></td>',
                day, events_html
            )

    def formatmonth(self, year, month):
        """Bootstrap対応の月のカレンダーHTMLを生成"""
        return f'<table class="table table-bordered text-center">{super().formatmonth(year, month)}</table>'
