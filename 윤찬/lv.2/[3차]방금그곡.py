import re
def solution(m, musicinfos):
    answer = ''
    m = re.sub('C#', 'c', m)
    m = re.sub('D#', 'd', m)
    m = re.sub('F#', 'f', m)
    m = re.sub('G#', 'g', m)
    m = re.sub('A#', 'a', m)
    c = re.compile(m)
    
    max_minute = 0
    
    for music_info in musicinfos:
        
        start_time, end_time, music_name, melody = music_info.split(',')
        start_hour, start_minute = map(int, start_time.split(':'))
        end_hour, end_minute = map(int, end_time.split(':'))
        minute = (end_hour * 60 + end_minute) - (start_hour * 60 + start_minute)
        
        melody = re.sub('C#', 'c', melody)
        melody = re.sub('D#', 'd', melody)
        melody = re.sub('F#', 'f', melody)
        melody = re.sub('G#', 'g', melody)
        melody = re.sub('A#', 'a', melody)
        size = len(melody)
        
        melody = melody[:minute] if minute <= size else melody * (minute//size) + melody[:(minute%size)]
        
        tmp = c.search(melody)
        
        if tmp != None and max_minute < minute:
            answer = music_name
            max_minute = minute
            
    return "(None)" if answer == '' else answer
