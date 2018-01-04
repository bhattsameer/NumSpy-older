from dashtable import html2rst
from requests import get, HTTPError
from argparse import ArgumentParser

api = "https://www.tricksfolks.com/truecaller/search.php?ccode=IN&number={number}"

def banner():
    print("""
 __    _  __   __  __   __  _______  _______  __   __ 
|  |  | ||  | |  ||  |_|  ||       ||       ||  | |  |
|   |_| ||  | |  ||       ||  _____||    _  ||  |_|  |
|       ||  |_|  ||       || |_____ |   |_| ||       |
|  _    ||       ||       ||_____  ||    ___||_     _|
| | |   ||       || ||_|| | _____| ||   |      |   |  
|_|  |__||_______||_|   |_||_______||___|      |___| 
        
        A truecaller Indian Number Search API
""")
    pass

def search_single(number, store=False, file=None):
    print("<--[ Searching Details For {} ]-->".format(number), end="\n\n")
    try:
        r = get(api.format(number=number))
        raw = r.content.decode()
        data = "<table>" + raw.split("<table>")[1].split("</table>")[0] + "</table>"
        op = html2rst(data)
        if store and file:
            with open(file, "w") as f:
                f.write("Phone Number Details For : {}\n\n".format(number))
                f.write(op)
                f.close()
            print("[!] Search Result is stored in {}".format(file))
        else:
            print(op) 
    except HTTPError as e:
        print("[x] Check Your Internet Connection")
    pass

def multiple_search(store=False, file=None, readfile=False):
    global f
    if file and store:
         f = open(file, "w")
    nums = [x for x in open(readfile, "r").read().split("\n") if x is not ""]
    for num in nums:
        print("\n<--[ Searching Details For {} ]-->".format(num), end="\n\n")
        try:
            r = get(api.format(number=num))
            raw = r.content.decode()
            data = "<table>" + raw.split("<table>")[1].split("</table>")[0] + "</table>"
            op = html2rst(data)
            if store and file:
                f.write("Phone Number Details For : {}\n".format(num))
                f.write(op)
                f.write("\n\n===============================================================\n\n")
                pass
            else:
                print(op)
        except HTTPError as e:
            print("[x] Check Your Internet Connection")
    if file and store:
        print("Saved seach result to {}".format(file))
            
    pass

def main():
    parser = ArgumentParser(description="A python program to find the details of number from truecaller")
    parser.add_argument("--number", help="Target number which you want to search", metavar="")
    parser.add_argument("-o", "--output", help="Output file name to store search results", metavar="")
    parser.add_argument("-r", help="Accepts a file name for bulk search\nNote: Store numbers line by name in file", metavar="")
    args = parser.parse_args()
    if args.number is None and args.r is None:
        parser.parse_args(["-h"])
    num = args.number
    file = args.r
    ofile = args.output
    if file is None and ofile is None:
        search_single(num)
    elif file is None and ofile is not None:
        search_single(num, store=True, file=ofile)
    elif file is not None and ofile is None:
        multiple_search(readfile=file)
    else:
        multiple_search(readfile=file, store=True, file=ofile)
    pass

if __name__ == '__main__':
    banner()
    main()