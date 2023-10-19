file = input("File Name :   ")
# print(file)
file = file.strip()
file = file.lower()
file = file.split(".")
# print(file)
x = len(file)
# print(x)
if x <= 1 :
    print("application/octet-stream")
else:
    match file[-1]:
        case "aac":
            print("audio/aac")
        case "abw":
            print("application/x-abiword")
        case "arc":
            print("application/x-freearc")
        case "avif":
            print("image/avif")
        case "avi":
            print("video/x-msvideo")
        case "azw":
            print("application/vnd.amazon.ebook")
        case ".bin":
            print("application/octet-stream")
        case "bmp":
            print("image/bmp")
        case "bz":
            print("application/x-bzip")
        case "bz2":
            print("application/x-bzip2")
        case "cda":
            print("application/x-cdf")
        case "csh":
            print("application/x-csh")
        case "css":
            print("text/css")
        case "csv":
            print("text/csv")
        case "doc":
            print("application/msword")
        case "docx":
            print("application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        case "eot":
            print("application/vnd.ms-fontobject")
        case "epub":
            print("application/epub+zip")
        case "gz":
            print("application/gzip")
        case "gif":
            print("image/gif")
        case "htm" | "html" :
            print("text/html")
        case "jpeg" | "jpg":
            print("image/jpeg")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case "pdf":
            print("application/pdf")
        case "png":
            print("image/png")
        case _:
            print("application/octet-stream")