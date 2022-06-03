import base64, sys
  
def encode(msg):
    sample_string_bytes = msg.encode("ascii")
    
    base64_bytes = base64.b64encode(sample_string_bytes)
    result = base64_bytes.decode("ascii")
    return result

def decode(msg):
    base64_string = msg
    base64_bytes = base64_string.encode("ascii")
    
    sample_string_bytes = base64.b64decode(base64_bytes)
    result = sample_string_bytes.decode("ascii")
    return result

def main():
    
    print('Press E for encoding and D for decoding. Any other character will quit program.')
    option = input()
    if(str.lower(option) == 'e'):
        msg ="Testing encryption"
        print(f"Result: {encode(msg)}")
    elif(str.lower(option) == 'd'):
        msg ="VGVzdGluZyBlbmNyeXB0aW9u"
        print(f"Result: {decode(msg)}")
    else:
        sys.exit()

if __name__ == '__main__':
   main()