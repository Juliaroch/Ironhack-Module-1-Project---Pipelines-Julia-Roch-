#Main.py
from acquisition import acquire
from wrangling import wrangle
from enrichment import enrich
from analyzing import analyze

def main():
    data = acquire()
    filtered = wrangle(data)
    enriched = enrich(filtered)
    results = analyze(enriched)

if __name__ == '__main__':
    main()