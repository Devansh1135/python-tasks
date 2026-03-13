from collections import Counter, defaultdict, deque, namedtuple

with open ("/home/devansh.jagatiya@simform.dom/python/file.txt") as f:
    words = f.read().split()
    f.seek(0)
    logs = [line.strip() for line in f]

# removing date-time values from the words list

filtered_words = [x for x in words if x.isalpha()]


# printing n most common words

c = Counter(filtered_words)
def mostcommon(dict, n):
    count = 0
    common = []
    for item in c.most_common():
        if count < n:
            common.append(item)
            count+=1
    return common

print(mostcommon(c,10))


# grouping words by first letter

groups = defaultdict(list)
for word in words:
    groups[word[0]].append(word)

print(groups.items())


# implementing buffer of length 100 using deque

buffer = deque(maxlen=100)
for i in range(120):
    buffer.append(i)

print(buffer)


# creating structured log entries using namedtuple

log = namedtuple("log", ['date', 'timestamp', 'log_level', 'message'])

structured_logs = []

for l in logs:
    date, time, level, *msg = l.split()
    message = " ".join(msg)
    entry = log(date, time, level, message)
    structured_logs.append(entry)

print(structured_logs)