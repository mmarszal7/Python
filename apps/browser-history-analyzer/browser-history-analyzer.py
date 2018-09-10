import os
import sqlite3
import operator
import matplotlib.pyplot as plt

def load_history():
    history_db = os.path.expanduser('~') + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
    c = sqlite3.connect(history_db)
    cursor = c.cursor()
    cursor.execute("SELECT url, visit_count FROM urls WHERE visit_count > 5")
    return cursor.fetchall()

def views_per_domain(history):
    domains = dict()
    for page in history:
        domain = page[0].split('/')[2]    
        print(domain)
        print(page[1])
        if domains and domain in domains:
            domains[domain] += page[1]
        else:
            domains[domain] = page[1]

    return sorted(domains.items(), key=operator.itemgetter(1), reverse = True)

def draw_graph(data):
    data = data[0:10]
    labels = [l[0] for l in data]
    sizes = [l[1] for l in data]
    
    # Plot
    plt.pie(sizes, shadow=True, startangle=140)
    patches, texts = plt.pie(sizes, shadow=True, startangle=90)
    plt.legend(patches, labels=labels, loc="best")
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    history = load_history()
    data = views_per_domain(history)
    draw_graph(data)