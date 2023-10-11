class AbstractChartAdapter:
    def render(self, data): ...

class XMLChart:
    def render(self, data): ...

class XMLChartAdapter:
    def __init__(self, adaptee: XMLChart) -> None:
        self.adaptee = adaptee
    
    def _convert_to_xml_format(self, data):
        # convert
        print("convert")
        return data

    def render(self, data):
        xml_data = self._convert_to_xml_format(data)
        return self.adaptee.render(xml_data)


json_data = "{foo: bar}"
adaptee = XMLChart()
chart = XMLChartAdapter(adaptee=adaptee)
chart.render(json_data)