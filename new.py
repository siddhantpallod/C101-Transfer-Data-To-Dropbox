import dropbox

class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def uploadFiles(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)
        file1 = open(fileFrom, 'rb')
        dbx.files_upload(file1.read(),fileTo)

def main():
    access_token = 'RZSCy2zyE_YAAAAAAAAAAf6OvC8czkqOFLqZ4N7miDA7lEFC7RGK4DLCShnX5sFo'
    transferData = TransferData(access_token)
    fileFrom = input("Enter The File Path To Be Uploaded: ")
    fileTo = input("Enter The Path To Uplaod To Dropbox: ")
    transferData.uploadFiles(fileFrom, fileTo)
    print("File has been copied!!")

if __name__ == '__main__':
    main()