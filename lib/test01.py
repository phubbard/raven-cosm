import file_reader
import echo

fr = file_reader.FileReader("testfile.xml")
fr.attach(echo.Echo())

fr.start()
fr.thread.join()

