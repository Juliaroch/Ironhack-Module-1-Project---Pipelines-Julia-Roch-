#Main.py
from Acquisition import acquire
from Wrangling import wrangle
from Enrichment import enrich
from Analyzing import analyze

def main():
    data = acquire()
    filtered = wrangle(data)
    enriched = enrich(filtered)
    results = analyze(enriched)

if __name__ == '__main__':
    main()