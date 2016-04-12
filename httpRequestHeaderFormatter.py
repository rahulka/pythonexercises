def prettyPrintHeaders(**kwargs):
    output = ""
    for k, v in kwargs.iteritems():
        output = output + str(k).replace("_", "-") + ":" + str(v) + "\n"
    return output

if __name__ == "__main__":
    print(prettyPrintHeaders(Accept="text/plain", Content_Length=10))