import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A4oIWECFKTiQptTGlGip4d2VT-1mi5NvEqri76H5iHTuDQH5bqBmP348gzLwI1_H4M_f632K4yf_uK5EYhS4XwQ7WMXrU1a_eIzdgBUFDaXwmx08jmrx9ZzPQiDI7W20RFLc46E'
    transferData = TransferData(access_token)

    file_from = input('Enter the file path to transfer:- ')
    file_to = input('Enter the full path to upload to dropbox:- ')
    
    #api V2 
    transferData.upload_file(file_from,file_to)
    print("File Has been moved!!")  


main()