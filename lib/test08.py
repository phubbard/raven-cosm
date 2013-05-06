import file_reader
import echo
import xml_tag_extractor

print """Test XMLTagExtractor with a file that starts partway through a fragment"""
fr = file_reader.FileReader("testfile2.xml")
fr.attach(xml_tag_extractor.XMLTagExtractor("InstantaneousDemand")).attach(echo.Echo())
fr.start()
fr.thread.join()

