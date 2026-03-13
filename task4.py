## Yielding lines of the file

def read_logs(filename):
    with open (f"/home/devansh.jagatiya@simform.dom/python/{filename}") as f:
        for line in f:
            yield line


lines = []
for line in read_logs("file.txt"):
    lines.append(line)


## Parsing logs as dictionaries 

def parse_logs(lines):

    for line in lines:
        date, time, level, *msg = line.split()

        yield {
            "date" : date,
            "time" : time,
            "level" : level,
            "message" : msg
        }
        
    
logs_dict = []
for item in parse_logs(lines):
    logs_dict.append(item)


## Logging only ERROR level logs

def filter_level(lines):
    for line in lines:
        date, time, level, *msg = line.split()
        if level == "ERROR":
            yield line


errors = filter_level(lines)


## Logging only the timestamps

def extract_timestamps(lines):
    for line in lines:
        date, time, level, *msg = line.split()
        yield time


timestamps = []

for i in extract_timestamps(lines):
    timestamps.append(i)
      
print(timestamps)