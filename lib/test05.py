import file_reader
import echo
import xml_tag_extractor
import datapoint_extractor

fr = file_reader.FileReader("testfile.xml")
idx = xml_tag_extractor.XMLTagExtractor("InstantaneousDemand")
dpx = datapoint_extractor.DatapointExtractor()

fr.attach(idx).attach(dpx).attach(echo.Echo())
fr.start()
fr.thread.join()

