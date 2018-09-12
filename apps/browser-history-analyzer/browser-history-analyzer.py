import os
import sqlite3
import operator
import matplotlib.pyplot as plt

ignore = ['www.', '.com', '.pl', '.net', '.uk']

def load_history():
    history_db = os.path.expanduser('~') + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
    c = sqlite3.connect(history_db)
    cursor = c.cursor()
    cursor.execute("SELECT url, visit_count FROM urls WHERE visit_count > 5 AND url NOT LIKE \"%localhost%\" AND url NOT LIKE \"%192%\"")
    return cursor.fetchall()

def views_per_domain(history):
    domains = dict()
    for page in history:
        domain = extract_domain(page)
        if domains and domain in domains:
            domains[domain] += page[1]
        else:
            domains[domain] = page[1]

    return sorted(domains.items(), key=operator.itemgetter(1), reverse = True)

def extract_domain(link):
	domain = link[0].split('/')[2]    
	for i in ignore:
		domain = domain.replace(i, '')
		
	return domain
	
def draw_graph(data):
    data = data[0:10]
    labels = [l[0] for l in data]
    sizes = [l[1] for l in data]
	
	labels.append('other')
	sizes.append(sum(views[1] for views in data[10:]))
    
    plt.pie(sizes, shadow=True, startangle=140)
    patches, texts = plt.pie(sizes, shadow=True, labels=labels, startangle=90)
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    history = load_history()
    data = views_per_domain(history)
    draw_graph(data)