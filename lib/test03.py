import file_reader
import echo
import xml_tag_extractor

fr = file_reader.FileReader("testfile.xml")
fr.attach(xml_tag_extractor.XMLTagExtractor("InstantaneousDemand")).attach(echo.Echo())
fr.start()
fr.thread.join()

