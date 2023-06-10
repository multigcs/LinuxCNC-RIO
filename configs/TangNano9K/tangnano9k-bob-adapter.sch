<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="9.0.1">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="15" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="88" name="SimResults" color="9" fill="1" visible="yes" active="yes"/>
<layer number="89" name="SimProbes" color="9" fill="1" visible="yes" active="yes"/>
<layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="pinhead" urn="urn:adsk.eagle:library:325">
<description>&lt;b&gt;Pin Header Connectors&lt;/b&gt;&lt;p&gt;
&lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
<package name="1X24" urn="urn:adsk.eagle:footprint:22324/1" library_version="3">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<wire x1="15.875" y1="1.27" x2="17.145" y2="1.27" width="0.1524" layer="21"/>
<wire x1="17.145" y1="1.27" x2="17.78" y2="0.635" width="0.1524" layer="21"/>
<wire x1="17.78" y1="0.635" x2="17.78" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="17.78" y1="-0.635" x2="17.145" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="12.7" y1="0.635" x2="13.335" y2="1.27" width="0.1524" layer="21"/>
<wire x1="13.335" y1="1.27" x2="14.605" y2="1.27" width="0.1524" layer="21"/>
<wire x1="14.605" y1="1.27" x2="15.24" y2="0.635" width="0.1524" layer="21"/>
<wire x1="15.24" y1="0.635" x2="15.24" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="15.24" y1="-0.635" x2="14.605" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="14.605" y1="-1.27" x2="13.335" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="13.335" y1="-1.27" x2="12.7" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="15.875" y1="1.27" x2="15.24" y2="0.635" width="0.1524" layer="21"/>
<wire x1="15.24" y1="-0.635" x2="15.875" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="17.145" y1="-1.27" x2="15.875" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="8.255" y1="1.27" x2="9.525" y2="1.27" width="0.1524" layer="21"/>
<wire x1="9.525" y1="1.27" x2="10.16" y2="0.635" width="0.1524" layer="21"/>
<wire x1="10.16" y1="0.635" x2="10.16" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="10.16" y1="-0.635" x2="9.525" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="10.16" y1="0.635" x2="10.795" y2="1.27" width="0.1524" layer="21"/>
<wire x1="10.795" y1="1.27" x2="12.065" y2="1.27" width="0.1524" layer="21"/>
<wire x1="12.065" y1="1.27" x2="12.7" y2="0.635" width="0.1524" layer="21"/>
<wire x1="12.7" y1="0.635" x2="12.7" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="12.7" y1="-0.635" x2="12.065" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="12.065" y1="-1.27" x2="10.795" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="10.795" y1="-1.27" x2="10.16" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="5.08" y1="0.635" x2="5.715" y2="1.27" width="0.1524" layer="21"/>
<wire x1="5.715" y1="1.27" x2="6.985" y2="1.27" width="0.1524" layer="21"/>
<wire x1="6.985" y1="1.27" x2="7.62" y2="0.635" width="0.1524" layer="21"/>
<wire x1="7.62" y1="0.635" x2="7.62" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="7.62" y1="-0.635" x2="6.985" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="6.985" y1="-1.27" x2="5.715" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="5.715" y1="-1.27" x2="5.08" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="8.255" y1="1.27" x2="7.62" y2="0.635" width="0.1524" layer="21"/>
<wire x1="7.62" y1="-0.635" x2="8.255" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="9.525" y1="-1.27" x2="8.255" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="0.635" y1="1.27" x2="1.905" y2="1.27" width="0.1524" layer="21"/>
<wire x1="1.905" y1="1.27" x2="2.54" y2="0.635" width="0.1524" layer="21"/>
<wire x1="2.54" y1="0.635" x2="2.54" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="2.54" y1="-0.635" x2="1.905" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="2.54" y1="0.635" x2="3.175" y2="1.27" width="0.1524" layer="21"/>
<wire x1="3.175" y1="1.27" x2="4.445" y2="1.27" width="0.1524" layer="21"/>
<wire x1="4.445" y1="1.27" x2="5.08" y2="0.635" width="0.1524" layer="21"/>
<wire x1="5.08" y1="0.635" x2="5.08" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="5.08" y1="-0.635" x2="4.445" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="4.445" y1="-1.27" x2="3.175" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="3.175" y1="-1.27" x2="2.54" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="0.635" x2="-1.905" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-1.905" y1="1.27" x2="-0.635" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-0.635" y1="1.27" x2="0" y2="0.635" width="0.1524" layer="21"/>
<wire x1="0" y1="0.635" x2="0" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="0" y1="-0.635" x2="-0.635" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-0.635" y1="-1.27" x2="-1.905" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-1.905" y1="-1.27" x2="-2.54" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="0.635" y1="1.27" x2="0" y2="0.635" width="0.1524" layer="21"/>
<wire x1="0" y1="-0.635" x2="0.635" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="1.905" y1="-1.27" x2="0.635" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-6.985" y1="1.27" x2="-5.715" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-5.715" y1="1.27" x2="-5.08" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-5.08" y1="0.635" x2="-5.08" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-5.08" y1="-0.635" x2="-5.715" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-5.08" y1="0.635" x2="-4.445" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-4.445" y1="1.27" x2="-3.175" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-3.175" y1="1.27" x2="-2.54" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="0.635" x2="-2.54" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="-0.635" x2="-3.175" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-3.175" y1="-1.27" x2="-4.445" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-4.445" y1="-1.27" x2="-5.08" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-10.16" y1="0.635" x2="-9.525" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-9.525" y1="1.27" x2="-8.255" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-8.255" y1="1.27" x2="-7.62" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-7.62" y1="0.635" x2="-7.62" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-7.62" y1="-0.635" x2="-8.255" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-8.255" y1="-1.27" x2="-9.525" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-9.525" y1="-1.27" x2="-10.16" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-6.985" y1="1.27" x2="-7.62" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-7.62" y1="-0.635" x2="-6.985" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-5.715" y1="-1.27" x2="-6.985" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-14.605" y1="1.27" x2="-13.335" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-13.335" y1="1.27" x2="-12.7" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-12.7" y1="0.635" x2="-12.7" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-12.7" y1="-0.635" x2="-13.335" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-12.7" y1="0.635" x2="-12.065" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-12.065" y1="1.27" x2="-10.795" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-10.795" y1="1.27" x2="-10.16" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-10.16" y1="0.635" x2="-10.16" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-10.16" y1="-0.635" x2="-10.795" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-10.795" y1="-1.27" x2="-12.065" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-12.065" y1="-1.27" x2="-12.7" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-17.78" y1="0.635" x2="-17.145" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-17.145" y1="1.27" x2="-15.875" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-15.875" y1="1.27" x2="-15.24" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-15.24" y1="0.635" x2="-15.24" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-15.24" y1="-0.635" x2="-15.875" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-15.875" y1="-1.27" x2="-17.145" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-17.145" y1="-1.27" x2="-17.78" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-14.605" y1="1.27" x2="-15.24" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-15.24" y1="-0.635" x2="-14.605" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-13.335" y1="-1.27" x2="-14.605" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-22.225" y1="1.27" x2="-20.955" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-20.955" y1="1.27" x2="-20.32" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-20.32" y1="0.635" x2="-20.32" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-20.32" y1="-0.635" x2="-20.955" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-20.32" y1="0.635" x2="-19.685" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-19.685" y1="1.27" x2="-18.415" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-18.415" y1="1.27" x2="-17.78" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-17.78" y1="0.635" x2="-17.78" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-17.78" y1="-0.635" x2="-18.415" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-18.415" y1="-1.27" x2="-19.685" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-19.685" y1="-1.27" x2="-20.32" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-25.4" y1="0.635" x2="-24.765" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-24.765" y1="1.27" x2="-23.495" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-23.495" y1="1.27" x2="-22.86" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-22.86" y1="0.635" x2="-22.86" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-22.86" y1="-0.635" x2="-23.495" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-23.495" y1="-1.27" x2="-24.765" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-24.765" y1="-1.27" x2="-25.4" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-22.225" y1="1.27" x2="-22.86" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-22.86" y1="-0.635" x2="-22.225" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-20.955" y1="-1.27" x2="-22.225" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-29.845" y1="1.27" x2="-28.575" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-28.575" y1="1.27" x2="-27.94" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-27.94" y1="0.635" x2="-27.94" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-27.94" y1="-0.635" x2="-28.575" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-27.94" y1="0.635" x2="-27.305" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-27.305" y1="1.27" x2="-26.035" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-26.035" y1="1.27" x2="-25.4" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-25.4" y1="0.635" x2="-25.4" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-25.4" y1="-0.635" x2="-26.035" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-26.035" y1="-1.27" x2="-27.305" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-27.305" y1="-1.27" x2="-27.94" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-30.48" y1="0.635" x2="-30.48" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-29.845" y1="1.27" x2="-30.48" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-30.48" y1="-0.635" x2="-29.845" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-28.575" y1="-1.27" x2="-29.845" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="18.415" y1="1.27" x2="19.685" y2="1.27" width="0.1524" layer="21"/>
<wire x1="19.685" y1="1.27" x2="20.32" y2="0.635" width="0.1524" layer="21"/>
<wire x1="20.32" y1="-0.635" x2="19.685" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="18.415" y1="1.27" x2="17.78" y2="0.635" width="0.1524" layer="21"/>
<wire x1="17.78" y1="-0.635" x2="18.415" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="19.685" y1="-1.27" x2="18.415" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="20.955" y1="1.27" x2="22.225" y2="1.27" width="0.1524" layer="21"/>
<wire x1="22.225" y1="1.27" x2="22.86" y2="0.635" width="0.1524" layer="21"/>
<wire x1="22.86" y1="0.635" x2="22.86" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="22.86" y1="-0.635" x2="22.225" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="20.32" y1="0.635" x2="20.32" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="20.955" y1="1.27" x2="20.32" y2="0.635" width="0.1524" layer="21"/>
<wire x1="20.32" y1="-0.635" x2="20.955" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="22.225" y1="-1.27" x2="20.955" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="23.495" y1="1.27" x2="24.765" y2="1.27" width="0.1524" layer="21"/>
<wire x1="24.765" y1="1.27" x2="25.4" y2="0.635" width="0.1524" layer="21"/>
<wire x1="25.4" y1="-0.635" x2="24.765" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="23.495" y1="1.27" x2="22.86" y2="0.635" width="0.1524" layer="21"/>
<wire x1="22.86" y1="-0.635" x2="23.495" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="24.765" y1="-1.27" x2="23.495" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="26.035" y1="1.27" x2="27.305" y2="1.27" width="0.1524" layer="21"/>
<wire x1="27.305" y1="1.27" x2="27.94" y2="0.635" width="0.1524" layer="21"/>
<wire x1="27.94" y1="0.635" x2="27.94" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="27.94" y1="-0.635" x2="27.305" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="25.4" y1="0.635" x2="25.4" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="26.035" y1="1.27" x2="25.4" y2="0.635" width="0.1524" layer="21"/>
<wire x1="25.4" y1="-0.635" x2="26.035" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="27.305" y1="-1.27" x2="26.035" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="28.575" y1="1.27" x2="29.845" y2="1.27" width="0.1524" layer="21"/>
<wire x1="29.845" y1="1.27" x2="30.48" y2="0.635" width="0.1524" layer="21"/>
<wire x1="30.48" y1="0.635" x2="30.48" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="30.48" y1="-0.635" x2="29.845" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="28.575" y1="1.27" x2="27.94" y2="0.635" width="0.1524" layer="21"/>
<wire x1="27.94" y1="-0.635" x2="28.575" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="29.845" y1="-1.27" x2="28.575" y2="-1.27" width="0.1524" layer="21"/>
<pad name="1" x="-29.21" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="2" x="-26.67" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="3" x="-24.13" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="4" x="-21.59" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="5" x="-19.05" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="6" x="-16.51" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="7" x="-13.97" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="8" x="-11.43" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="9" x="-8.89" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="10" x="-6.35" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="11" x="-3.81" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="12" x="-1.27" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="13" x="1.27" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="14" x="3.81" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="15" x="6.35" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="16" x="8.89" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="17" x="11.43" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="18" x="13.97" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="19" x="16.51" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="20" x="19.05" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="21" x="21.59" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="22" x="24.13" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="23" x="26.67" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="24" x="29.21" y="0" drill="1.016" shape="long" rot="R90"/>
<text x="-30.5562" y="1.8288" size="1.27" layer="25" ratio="10">&gt;NAME</text>
<text x="-30.48" y="-3.175" size="1.27" layer="27">&gt;VALUE</text>
<rectangle x1="16.256" y1="-0.254" x2="16.764" y2="0.254" layer="51"/>
<rectangle x1="13.716" y1="-0.254" x2="14.224" y2="0.254" layer="51"/>
<rectangle x1="11.176" y1="-0.254" x2="11.684" y2="0.254" layer="51"/>
<rectangle x1="8.636" y1="-0.254" x2="9.144" y2="0.254" layer="51"/>
<rectangle x1="6.096" y1="-0.254" x2="6.604" y2="0.254" layer="51"/>
<rectangle x1="3.556" y1="-0.254" x2="4.064" y2="0.254" layer="51"/>
<rectangle x1="1.016" y1="-0.254" x2="1.524" y2="0.254" layer="51"/>
<rectangle x1="-1.524" y1="-0.254" x2="-1.016" y2="0.254" layer="51"/>
<rectangle x1="-4.064" y1="-0.254" x2="-3.556" y2="0.254" layer="51"/>
<rectangle x1="-6.604" y1="-0.254" x2="-6.096" y2="0.254" layer="51"/>
<rectangle x1="-9.144" y1="-0.254" x2="-8.636" y2="0.254" layer="51"/>
<rectangle x1="-11.684" y1="-0.254" x2="-11.176" y2="0.254" layer="51"/>
<rectangle x1="-14.224" y1="-0.254" x2="-13.716" y2="0.254" layer="51"/>
<rectangle x1="-16.764" y1="-0.254" x2="-16.256" y2="0.254" layer="51"/>
<rectangle x1="-19.304" y1="-0.254" x2="-18.796" y2="0.254" layer="51"/>
<rectangle x1="-21.844" y1="-0.254" x2="-21.336" y2="0.254" layer="51"/>
<rectangle x1="-24.384" y1="-0.254" x2="-23.876" y2="0.254" layer="51"/>
<rectangle x1="-26.924" y1="-0.254" x2="-26.416" y2="0.254" layer="51"/>
<rectangle x1="-29.464" y1="-0.254" x2="-28.956" y2="0.254" layer="51"/>
<rectangle x1="18.796" y1="-0.254" x2="19.304" y2="0.254" layer="51"/>
<rectangle x1="21.336" y1="-0.254" x2="21.844" y2="0.254" layer="51"/>
<rectangle x1="23.876" y1="-0.254" x2="24.384" y2="0.254" layer="51"/>
<rectangle x1="26.416" y1="-0.254" x2="26.924" y2="0.254" layer="51"/>
<rectangle x1="28.956" y1="-0.254" x2="29.464" y2="0.254" layer="51"/>
</package>
<package name="1X24/90" urn="urn:adsk.eagle:footprint:22325/1" library_version="3">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<wire x1="-30.48" y1="-1.905" x2="-27.94" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-27.94" y1="-1.905" x2="-27.94" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-27.94" y1="0.635" x2="-30.48" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-30.48" y1="0.635" x2="-30.48" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-29.21" y1="6.985" x2="-29.21" y2="1.27" width="0.762" layer="21"/>
<wire x1="-27.94" y1="-1.905" x2="-25.4" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-25.4" y1="-1.905" x2="-25.4" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-25.4" y1="0.635" x2="-27.94" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-26.67" y1="6.985" x2="-26.67" y2="1.27" width="0.762" layer="21"/>
<wire x1="-25.4" y1="-1.905" x2="-22.86" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-22.86" y1="-1.905" x2="-22.86" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-22.86" y1="0.635" x2="-25.4" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-24.13" y1="6.985" x2="-24.13" y2="1.27" width="0.762" layer="21"/>
<wire x1="-22.86" y1="-1.905" x2="-20.32" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-20.32" y1="-1.905" x2="-20.32" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-20.32" y1="0.635" x2="-22.86" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-21.59" y1="6.985" x2="-21.59" y2="1.27" width="0.762" layer="21"/>
<wire x1="-20.32" y1="-1.905" x2="-17.78" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-17.78" y1="-1.905" x2="-17.78" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-17.78" y1="0.635" x2="-20.32" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-19.05" y1="6.985" x2="-19.05" y2="1.27" width="0.762" layer="21"/>
<wire x1="-17.78" y1="-1.905" x2="-15.24" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-15.24" y1="-1.905" x2="-15.24" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-15.24" y1="0.635" x2="-17.78" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-16.51" y1="6.985" x2="-16.51" y2="1.27" width="0.762" layer="21"/>
<wire x1="-15.24" y1="-1.905" x2="-12.7" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-12.7" y1="-1.905" x2="-12.7" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-12.7" y1="0.635" x2="-15.24" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-13.97" y1="6.985" x2="-13.97" y2="1.27" width="0.762" layer="21"/>
<wire x1="-12.7" y1="-1.905" x2="-10.16" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-10.16" y1="-1.905" x2="-10.16" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-10.16" y1="0.635" x2="-12.7" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-11.43" y1="6.985" x2="-11.43" y2="1.27" width="0.762" layer="21"/>
<wire x1="-10.16" y1="-1.905" x2="-7.62" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-7.62" y1="-1.905" x2="-7.62" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-7.62" y1="0.635" x2="-10.16" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-8.89" y1="6.985" x2="-8.89" y2="1.27" width="0.762" layer="21"/>
<wire x1="-7.62" y1="-1.905" x2="-5.08" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-5.08" y1="-1.905" x2="-5.08" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-5.08" y1="0.635" x2="-7.62" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-6.35" y1="6.985" x2="-6.35" y2="1.27" width="0.762" layer="21"/>
<wire x1="-5.08" y1="-1.905" x2="-2.54" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="-1.905" x2="-2.54" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="0.635" x2="-5.08" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="6.985" x2="-3.81" y2="1.27" width="0.762" layer="21"/>
<wire x1="-2.54" y1="-1.905" x2="0" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="0" y1="-1.905" x2="0" y2="0.635" width="0.1524" layer="21"/>
<wire x1="0" y1="0.635" x2="-2.54" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="6.985" x2="-1.27" y2="1.27" width="0.762" layer="21"/>
<wire x1="0" y1="-1.905" x2="2.54" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="2.54" y1="-1.905" x2="2.54" y2="0.635" width="0.1524" layer="21"/>
<wire x1="2.54" y1="0.635" x2="0" y2="0.635" width="0.1524" layer="21"/>
<wire x1="1.27" y1="6.985" x2="1.27" y2="1.27" width="0.762" layer="21"/>
<wire x1="2.54" y1="-1.905" x2="5.08" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="5.08" y1="-1.905" x2="5.08" y2="0.635" width="0.1524" layer="21"/>
<wire x1="5.08" y1="0.635" x2="2.54" y2="0.635" width="0.1524" layer="21"/>
<wire x1="3.81" y1="6.985" x2="3.81" y2="1.27" width="0.762" layer="21"/>
<wire x1="5.08" y1="-1.905" x2="7.62" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="7.62" y1="-1.905" x2="7.62" y2="0.635" width="0.1524" layer="21"/>
<wire x1="7.62" y1="0.635" x2="5.08" y2="0.635" width="0.1524" layer="21"/>
<wire x1="6.35" y1="6.985" x2="6.35" y2="1.27" width="0.762" layer="21"/>
<wire x1="7.62" y1="-1.905" x2="10.16" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="10.16" y1="-1.905" x2="10.16" y2="0.635" width="0.1524" layer="21"/>
<wire x1="10.16" y1="0.635" x2="7.62" y2="0.635" width="0.1524" layer="21"/>
<wire x1="8.89" y1="6.985" x2="8.89" y2="1.27" width="0.762" layer="21"/>
<wire x1="10.16" y1="-1.905" x2="12.7" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="12.7" y1="-1.905" x2="12.7" y2="0.635" width="0.1524" layer="21"/>
<wire x1="12.7" y1="0.635" x2="10.16" y2="0.635" width="0.1524" layer="21"/>
<wire x1="11.43" y1="6.985" x2="11.43" y2="1.27" width="0.762" layer="21"/>
<wire x1="12.7" y1="-1.905" x2="15.24" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="15.24" y1="-1.905" x2="15.24" y2="0.635" width="0.1524" layer="21"/>
<wire x1="15.24" y1="0.635" x2="12.7" y2="0.635" width="0.1524" layer="21"/>
<wire x1="13.97" y1="6.985" x2="13.97" y2="1.27" width="0.762" layer="21"/>
<wire x1="15.24" y1="-1.905" x2="17.78" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="17.78" y1="-1.905" x2="17.78" y2="0.635" width="0.1524" layer="21"/>
<wire x1="17.78" y1="0.635" x2="15.24" y2="0.635" width="0.1524" layer="21"/>
<wire x1="16.51" y1="6.985" x2="16.51" y2="1.27" width="0.762" layer="21"/>
<wire x1="17.78" y1="-1.905" x2="20.32" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="20.32" y1="-1.905" x2="20.32" y2="0.635" width="0.1524" layer="21"/>
<wire x1="20.32" y1="0.635" x2="17.78" y2="0.635" width="0.1524" layer="21"/>
<wire x1="19.05" y1="6.985" x2="19.05" y2="1.27" width="0.762" layer="21"/>
<wire x1="20.32" y1="-1.905" x2="22.86" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="22.86" y1="-1.905" x2="22.86" y2="0.635" width="0.1524" layer="21"/>
<wire x1="22.86" y1="0.635" x2="20.32" y2="0.635" width="0.1524" layer="21"/>
<wire x1="21.59" y1="6.985" x2="21.59" y2="1.27" width="0.762" layer="21"/>
<wire x1="22.86" y1="-1.905" x2="25.4" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="25.4" y1="-1.905" x2="25.4" y2="0.635" width="0.1524" layer="21"/>
<wire x1="25.4" y1="0.635" x2="22.86" y2="0.635" width="0.1524" layer="21"/>
<wire x1="24.13" y1="6.985" x2="24.13" y2="1.27" width="0.762" layer="21"/>
<wire x1="25.4" y1="-1.905" x2="27.94" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="27.94" y1="-1.905" x2="27.94" y2="0.635" width="0.1524" layer="21"/>
<wire x1="27.94" y1="0.635" x2="25.4" y2="0.635" width="0.1524" layer="21"/>
<wire x1="26.67" y1="6.985" x2="26.67" y2="1.27" width="0.762" layer="21"/>
<wire x1="27.94" y1="-1.905" x2="30.48" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="30.48" y1="-1.905" x2="30.48" y2="0.635" width="0.1524" layer="21"/>
<wire x1="30.48" y1="0.635" x2="27.94" y2="0.635" width="0.1524" layer="21"/>
<wire x1="29.21" y1="6.985" x2="29.21" y2="1.27" width="0.762" layer="21"/>
<pad name="1" x="-29.21" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="2" x="-26.67" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="3" x="-24.13" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="4" x="-21.59" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="5" x="-19.05" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="6" x="-16.51" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="7" x="-13.97" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="8" x="-11.43" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="9" x="-8.89" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="10" x="-6.35" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="11" x="-3.81" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="12" x="-1.27" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="13" x="1.27" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="14" x="3.81" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="15" x="6.35" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="16" x="8.89" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="17" x="11.43" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="18" x="13.97" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="19" x="16.51" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="20" x="19.05" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="21" x="21.59" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="22" x="24.13" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="23" x="26.67" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="24" x="29.21" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<text x="-31.115" y="-3.81" size="1.27" layer="25" ratio="10" rot="R90">&gt;NAME</text>
<text x="32.385" y="-3.81" size="1.27" layer="27" rot="R90">&gt;VALUE</text>
<rectangle x1="-29.591" y1="0.635" x2="-28.829" y2="1.143" layer="21"/>
<rectangle x1="-27.051" y1="0.635" x2="-26.289" y2="1.143" layer="21"/>
<rectangle x1="-24.511" y1="0.635" x2="-23.749" y2="1.143" layer="21"/>
<rectangle x1="-21.971" y1="0.635" x2="-21.209" y2="1.143" layer="21"/>
<rectangle x1="-19.431" y1="0.635" x2="-18.669" y2="1.143" layer="21"/>
<rectangle x1="-16.891" y1="0.635" x2="-16.129" y2="1.143" layer="21"/>
<rectangle x1="-14.351" y1="0.635" x2="-13.589" y2="1.143" layer="21"/>
<rectangle x1="-11.811" y1="0.635" x2="-11.049" y2="1.143" layer="21"/>
<rectangle x1="-9.271" y1="0.635" x2="-8.509" y2="1.143" layer="21"/>
<rectangle x1="-6.731" y1="0.635" x2="-5.969" y2="1.143" layer="21"/>
<rectangle x1="-4.191" y1="0.635" x2="-3.429" y2="1.143" layer="21"/>
<rectangle x1="-1.651" y1="0.635" x2="-0.889" y2="1.143" layer="21"/>
<rectangle x1="0.889" y1="0.635" x2="1.651" y2="1.143" layer="21"/>
<rectangle x1="3.429" y1="0.635" x2="4.191" y2="1.143" layer="21"/>
<rectangle x1="5.969" y1="0.635" x2="6.731" y2="1.143" layer="21"/>
<rectangle x1="8.509" y1="0.635" x2="9.271" y2="1.143" layer="21"/>
<rectangle x1="11.049" y1="0.635" x2="11.811" y2="1.143" layer="21"/>
<rectangle x1="13.589" y1="0.635" x2="14.351" y2="1.143" layer="21"/>
<rectangle x1="16.129" y1="0.635" x2="16.891" y2="1.143" layer="21"/>
<rectangle x1="18.669" y1="0.635" x2="19.431" y2="1.143" layer="21"/>
<rectangle x1="-29.591" y1="-2.921" x2="-28.829" y2="-1.905" layer="21"/>
<rectangle x1="-27.051" y1="-2.921" x2="-26.289" y2="-1.905" layer="21"/>
<rectangle x1="-24.511" y1="-2.921" x2="-23.749" y2="-1.905" layer="21"/>
<rectangle x1="-21.971" y1="-2.921" x2="-21.209" y2="-1.905" layer="21"/>
<rectangle x1="-19.431" y1="-2.921" x2="-18.669" y2="-1.905" layer="21"/>
<rectangle x1="-16.891" y1="-2.921" x2="-16.129" y2="-1.905" layer="21"/>
<rectangle x1="-14.351" y1="-2.921" x2="-13.589" y2="-1.905" layer="21"/>
<rectangle x1="-11.811" y1="-2.921" x2="-11.049" y2="-1.905" layer="21"/>
<rectangle x1="-9.271" y1="-2.921" x2="-8.509" y2="-1.905" layer="21"/>
<rectangle x1="-6.731" y1="-2.921" x2="-5.969" y2="-1.905" layer="21"/>
<rectangle x1="-4.191" y1="-2.921" x2="-3.429" y2="-1.905" layer="21"/>
<rectangle x1="-1.651" y1="-2.921" x2="-0.889" y2="-1.905" layer="21"/>
<rectangle x1="0.889" y1="-2.921" x2="1.651" y2="-1.905" layer="21"/>
<rectangle x1="3.429" y1="-2.921" x2="4.191" y2="-1.905" layer="21"/>
<rectangle x1="5.969" y1="-2.921" x2="6.731" y2="-1.905" layer="21"/>
<rectangle x1="8.509" y1="-2.921" x2="9.271" y2="-1.905" layer="21"/>
<rectangle x1="11.049" y1="-2.921" x2="11.811" y2="-1.905" layer="21"/>
<rectangle x1="13.589" y1="-2.921" x2="14.351" y2="-1.905" layer="21"/>
<rectangle x1="16.129" y1="-2.921" x2="16.891" y2="-1.905" layer="21"/>
<rectangle x1="18.669" y1="-2.921" x2="19.431" y2="-1.905" layer="21"/>
<rectangle x1="21.209" y1="0.635" x2="21.971" y2="1.143" layer="21"/>
<rectangle x1="23.749" y1="0.635" x2="24.511" y2="1.143" layer="21"/>
<rectangle x1="21.209" y1="-2.921" x2="21.971" y2="-1.905" layer="21"/>
<rectangle x1="23.749" y1="-2.921" x2="24.511" y2="-1.905" layer="21"/>
<rectangle x1="26.289" y1="0.635" x2="27.051" y2="1.143" layer="21"/>
<rectangle x1="28.829" y1="0.635" x2="29.591" y2="1.143" layer="21"/>
<rectangle x1="26.289" y1="-2.921" x2="27.051" y2="-1.905" layer="21"/>
<rectangle x1="28.829" y1="-2.921" x2="29.591" y2="-1.905" layer="21"/>
</package>
<package name="1X06" urn="urn:adsk.eagle:footprint:22361/1" library_version="3">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<wire x1="0.635" y1="1.27" x2="1.905" y2="1.27" width="0.1524" layer="21"/>
<wire x1="1.905" y1="1.27" x2="2.54" y2="0.635" width="0.1524" layer="21"/>
<wire x1="2.54" y1="0.635" x2="2.54" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="2.54" y1="-0.635" x2="1.905" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="2.54" y1="0.635" x2="3.175" y2="1.27" width="0.1524" layer="21"/>
<wire x1="3.175" y1="1.27" x2="4.445" y2="1.27" width="0.1524" layer="21"/>
<wire x1="4.445" y1="1.27" x2="5.08" y2="0.635" width="0.1524" layer="21"/>
<wire x1="5.08" y1="0.635" x2="5.08" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="5.08" y1="-0.635" x2="4.445" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="4.445" y1="-1.27" x2="3.175" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="3.175" y1="-1.27" x2="2.54" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="0.635" x2="-1.905" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-1.905" y1="1.27" x2="-0.635" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-0.635" y1="1.27" x2="0" y2="0.635" width="0.1524" layer="21"/>
<wire x1="0" y1="0.635" x2="0" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="0" y1="-0.635" x2="-0.635" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-0.635" y1="-1.27" x2="-1.905" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-1.905" y1="-1.27" x2="-2.54" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="0.635" y1="1.27" x2="0" y2="0.635" width="0.1524" layer="21"/>
<wire x1="0" y1="-0.635" x2="0.635" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="1.905" y1="-1.27" x2="0.635" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-6.985" y1="1.27" x2="-5.715" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-5.715" y1="1.27" x2="-5.08" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-5.08" y1="0.635" x2="-5.08" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-5.08" y1="-0.635" x2="-5.715" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-5.08" y1="0.635" x2="-4.445" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-4.445" y1="1.27" x2="-3.175" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-3.175" y1="1.27" x2="-2.54" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="0.635" x2="-2.54" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="-0.635" x2="-3.175" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-3.175" y1="-1.27" x2="-4.445" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-4.445" y1="-1.27" x2="-5.08" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-7.62" y1="0.635" x2="-7.62" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-6.985" y1="1.27" x2="-7.62" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-7.62" y1="-0.635" x2="-6.985" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-5.715" y1="-1.27" x2="-6.985" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="5.715" y1="1.27" x2="6.985" y2="1.27" width="0.1524" layer="21"/>
<wire x1="6.985" y1="1.27" x2="7.62" y2="0.635" width="0.1524" layer="21"/>
<wire x1="7.62" y1="0.635" x2="7.62" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="7.62" y1="-0.635" x2="6.985" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="5.715" y1="1.27" x2="5.08" y2="0.635" width="0.1524" layer="21"/>
<wire x1="5.08" y1="-0.635" x2="5.715" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="6.985" y1="-1.27" x2="5.715" y2="-1.27" width="0.1524" layer="21"/>
<pad name="1" x="-6.35" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="2" x="-3.81" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="3" x="-1.27" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="4" x="1.27" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="5" x="3.81" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="6" x="6.35" y="0" drill="1.016" shape="long" rot="R90"/>
<text x="-7.6962" y="1.8288" size="1.27" layer="25" ratio="10">&gt;NAME</text>
<text x="-7.62" y="-3.175" size="1.27" layer="27">&gt;VALUE</text>
<rectangle x1="3.556" y1="-0.254" x2="4.064" y2="0.254" layer="51"/>
<rectangle x1="1.016" y1="-0.254" x2="1.524" y2="0.254" layer="51"/>
<rectangle x1="-1.524" y1="-0.254" x2="-1.016" y2="0.254" layer="51"/>
<rectangle x1="-4.064" y1="-0.254" x2="-3.556" y2="0.254" layer="51"/>
<rectangle x1="-6.604" y1="-0.254" x2="-6.096" y2="0.254" layer="51"/>
<rectangle x1="6.096" y1="-0.254" x2="6.604" y2="0.254" layer="51"/>
</package>
<package name="1X06/90" urn="urn:adsk.eagle:footprint:22362/1" library_version="3">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<wire x1="-7.62" y1="-1.905" x2="-5.08" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-5.08" y1="-1.905" x2="-5.08" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-5.08" y1="0.635" x2="-7.62" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-7.62" y1="0.635" x2="-7.62" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-6.35" y1="6.985" x2="-6.35" y2="1.27" width="0.762" layer="21"/>
<wire x1="-5.08" y1="-1.905" x2="-2.54" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="-1.905" x2="-2.54" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="0.635" x2="-5.08" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="6.985" x2="-3.81" y2="1.27" width="0.762" layer="21"/>
<wire x1="-2.54" y1="-1.905" x2="0" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="0" y1="-1.905" x2="0" y2="0.635" width="0.1524" layer="21"/>
<wire x1="0" y1="0.635" x2="-2.54" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="6.985" x2="-1.27" y2="1.27" width="0.762" layer="21"/>
<wire x1="0" y1="-1.905" x2="2.54" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="2.54" y1="-1.905" x2="2.54" y2="0.635" width="0.1524" layer="21"/>
<wire x1="2.54" y1="0.635" x2="0" y2="0.635" width="0.1524" layer="21"/>
<wire x1="1.27" y1="6.985" x2="1.27" y2="1.27" width="0.762" layer="21"/>
<wire x1="2.54" y1="-1.905" x2="5.08" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="5.08" y1="-1.905" x2="5.08" y2="0.635" width="0.1524" layer="21"/>
<wire x1="5.08" y1="0.635" x2="2.54" y2="0.635" width="0.1524" layer="21"/>
<wire x1="3.81" y1="6.985" x2="3.81" y2="1.27" width="0.762" layer="21"/>
<wire x1="5.08" y1="-1.905" x2="7.62" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="7.62" y1="-1.905" x2="7.62" y2="0.635" width="0.1524" layer="21"/>
<wire x1="7.62" y1="0.635" x2="5.08" y2="0.635" width="0.1524" layer="21"/>
<wire x1="6.35" y1="6.985" x2="6.35" y2="1.27" width="0.762" layer="21"/>
<pad name="1" x="-6.35" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="2" x="-3.81" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="3" x="-1.27" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="4" x="1.27" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="5" x="3.81" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="6" x="6.35" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<text x="-8.255" y="-3.81" size="1.27" layer="25" ratio="10" rot="R90">&gt;NAME</text>
<text x="9.525" y="-3.81" size="1.27" layer="27" rot="R90">&gt;VALUE</text>
<rectangle x1="-6.731" y1="0.635" x2="-5.969" y2="1.143" layer="21"/>
<rectangle x1="-4.191" y1="0.635" x2="-3.429" y2="1.143" layer="21"/>
<rectangle x1="-1.651" y1="0.635" x2="-0.889" y2="1.143" layer="21"/>
<rectangle x1="0.889" y1="0.635" x2="1.651" y2="1.143" layer="21"/>
<rectangle x1="3.429" y1="0.635" x2="4.191" y2="1.143" layer="21"/>
<rectangle x1="5.969" y1="0.635" x2="6.731" y2="1.143" layer="21"/>
<rectangle x1="-6.731" y1="-2.921" x2="-5.969" y2="-1.905" layer="21"/>
<rectangle x1="-4.191" y1="-2.921" x2="-3.429" y2="-1.905" layer="21"/>
<rectangle x1="-1.651" y1="-2.921" x2="-0.889" y2="-1.905" layer="21"/>
<rectangle x1="0.889" y1="-2.921" x2="1.651" y2="-1.905" layer="21"/>
<rectangle x1="3.429" y1="-2.921" x2="4.191" y2="-1.905" layer="21"/>
<rectangle x1="5.969" y1="-2.921" x2="6.731" y2="-1.905" layer="21"/>
</package>
<package name="1X02" urn="urn:adsk.eagle:footprint:22309/1" library_version="3">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<wire x1="-1.905" y1="1.27" x2="-0.635" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-0.635" y1="1.27" x2="0" y2="0.635" width="0.1524" layer="21"/>
<wire x1="0" y1="0.635" x2="0" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="0" y1="-0.635" x2="-0.635" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="0.635" x2="-2.54" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-1.905" y1="1.27" x2="-2.54" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="-0.635" x2="-1.905" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-0.635" y1="-1.27" x2="-1.905" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="0" y1="0.635" x2="0.635" y2="1.27" width="0.1524" layer="21"/>
<wire x1="0.635" y1="1.27" x2="1.905" y2="1.27" width="0.1524" layer="21"/>
<wire x1="1.905" y1="1.27" x2="2.54" y2="0.635" width="0.1524" layer="21"/>
<wire x1="2.54" y1="0.635" x2="2.54" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="2.54" y1="-0.635" x2="1.905" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="1.905" y1="-1.27" x2="0.635" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="0.635" y1="-1.27" x2="0" y2="-0.635" width="0.1524" layer="21"/>
<pad name="1" x="-1.27" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="2" x="1.27" y="0" drill="1.016" shape="long" rot="R90"/>
<text x="-2.6162" y="1.8288" size="1.27" layer="25" ratio="10">&gt;NAME</text>
<text x="-2.54" y="-3.175" size="1.27" layer="27">&gt;VALUE</text>
<rectangle x1="-1.524" y1="-0.254" x2="-1.016" y2="0.254" layer="51"/>
<rectangle x1="1.016" y1="-0.254" x2="1.524" y2="0.254" layer="51"/>
</package>
<package name="1X02/90" urn="urn:adsk.eagle:footprint:22310/1" library_version="3">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<wire x1="-2.54" y1="-1.905" x2="0" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="0" y1="-1.905" x2="0" y2="0.635" width="0.1524" layer="21"/>
<wire x1="0" y1="0.635" x2="-2.54" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="0.635" x2="-2.54" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="6.985" x2="-1.27" y2="1.27" width="0.762" layer="21"/>
<wire x1="0" y1="-1.905" x2="2.54" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="2.54" y1="-1.905" x2="2.54" y2="0.635" width="0.1524" layer="21"/>
<wire x1="2.54" y1="0.635" x2="0" y2="0.635" width="0.1524" layer="21"/>
<wire x1="1.27" y1="6.985" x2="1.27" y2="1.27" width="0.762" layer="21"/>
<pad name="1" x="-1.27" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="2" x="1.27" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<text x="-3.175" y="-3.81" size="1.27" layer="25" ratio="10" rot="R90">&gt;NAME</text>
<text x="4.445" y="-3.81" size="1.27" layer="27" rot="R90">&gt;VALUE</text>
<rectangle x1="-1.651" y1="0.635" x2="-0.889" y2="1.143" layer="21"/>
<rectangle x1="0.889" y1="0.635" x2="1.651" y2="1.143" layer="21"/>
<rectangle x1="-1.651" y1="-2.921" x2="-0.889" y2="-1.905" layer="21"/>
<rectangle x1="0.889" y1="-2.921" x2="1.651" y2="-1.905" layer="21"/>
</package>
</packages>
<packages3d>
<package3d name="1X24" urn="urn:adsk.eagle:package:22448/2" type="model" library_version="3">
<description>PIN HEADER</description>
<packageinstances>
<packageinstance name="1X24"/>
</packageinstances>
</package3d>
<package3d name="1X24/90" urn="urn:adsk.eagle:package:22449/2" type="model" library_version="3">
<description>PIN HEADER</description>
<packageinstances>
<packageinstance name="1X24/90"/>
</packageinstances>
</package3d>
<package3d name="1X06" urn="urn:adsk.eagle:package:22472/2" type="model" library_version="3">
<description>PIN HEADER</description>
<packageinstances>
<packageinstance name="1X06"/>
</packageinstances>
</package3d>
<package3d name="1X06/90" urn="urn:adsk.eagle:package:22475/2" type="model" library_version="3">
<description>PIN HEADER</description>
<packageinstances>
<packageinstance name="1X06/90"/>
</packageinstances>
</package3d>
<package3d name="1X02" urn="urn:adsk.eagle:package:22435/2" type="model" library_version="3">
<description>PIN HEADER</description>
<packageinstances>
<packageinstance name="1X02"/>
</packageinstances>
</package3d>
<package3d name="1X02/90" urn="urn:adsk.eagle:package:22437/2" type="model" library_version="3">
<description>PIN HEADER</description>
<packageinstances>
<packageinstance name="1X02/90"/>
</packageinstances>
</package3d>
</packages3d>
<symbols>
<symbol name="PINHD24" urn="urn:adsk.eagle:symbol:22323/1" library_version="3">
<wire x1="-6.35" y1="-33.02" x2="1.27" y2="-33.02" width="0.4064" layer="94"/>
<wire x1="1.27" y1="-33.02" x2="1.27" y2="30.48" width="0.4064" layer="94"/>
<wire x1="1.27" y1="30.48" x2="-6.35" y2="30.48" width="0.4064" layer="94"/>
<wire x1="-6.35" y1="30.48" x2="-6.35" y2="-33.02" width="0.4064" layer="94"/>
<text x="-6.35" y="31.115" size="1.778" layer="95">&gt;NAME</text>
<text x="-6.35" y="-35.56" size="1.778" layer="96">&gt;VALUE</text>
<pin name="1" x="-2.54" y="27.94" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="2" x="-2.54" y="25.4" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="3" x="-2.54" y="22.86" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="4" x="-2.54" y="20.32" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="5" x="-2.54" y="17.78" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="6" x="-2.54" y="15.24" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="7" x="-2.54" y="12.7" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="8" x="-2.54" y="10.16" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="9" x="-2.54" y="7.62" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="10" x="-2.54" y="5.08" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="11" x="-2.54" y="2.54" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="12" x="-2.54" y="0" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="13" x="-2.54" y="-2.54" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="14" x="-2.54" y="-5.08" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="15" x="-2.54" y="-7.62" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="16" x="-2.54" y="-10.16" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="17" x="-2.54" y="-12.7" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="18" x="-2.54" y="-15.24" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="19" x="-2.54" y="-17.78" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="20" x="-2.54" y="-20.32" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="21" x="-2.54" y="-22.86" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="22" x="-2.54" y="-25.4" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="23" x="-2.54" y="-27.94" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="24" x="-2.54" y="-30.48" visible="pad" length="short" direction="pas" function="dot"/>
</symbol>
<symbol name="PINHD6" urn="urn:adsk.eagle:symbol:22360/1" library_version="3">
<wire x1="-6.35" y1="-7.62" x2="1.27" y2="-7.62" width="0.4064" layer="94"/>
<wire x1="1.27" y1="-7.62" x2="1.27" y2="10.16" width="0.4064" layer="94"/>
<wire x1="1.27" y1="10.16" x2="-6.35" y2="10.16" width="0.4064" layer="94"/>
<wire x1="-6.35" y1="10.16" x2="-6.35" y2="-7.62" width="0.4064" layer="94"/>
<text x="-6.35" y="10.795" size="1.778" layer="95">&gt;NAME</text>
<text x="-6.35" y="-10.16" size="1.778" layer="96">&gt;VALUE</text>
<pin name="1" x="-2.54" y="7.62" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="2" x="-2.54" y="5.08" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="3" x="-2.54" y="2.54" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="4" x="-2.54" y="0" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="5" x="-2.54" y="-2.54" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="6" x="-2.54" y="-5.08" visible="pad" length="short" direction="pas" function="dot"/>
</symbol>
<symbol name="PINHD2" urn="urn:adsk.eagle:symbol:22308/1" library_version="3">
<wire x1="-6.35" y1="-2.54" x2="1.27" y2="-2.54" width="0.4064" layer="94"/>
<wire x1="1.27" y1="-2.54" x2="1.27" y2="5.08" width="0.4064" layer="94"/>
<wire x1="1.27" y1="5.08" x2="-6.35" y2="5.08" width="0.4064" layer="94"/>
<wire x1="-6.35" y1="5.08" x2="-6.35" y2="-2.54" width="0.4064" layer="94"/>
<text x="-6.35" y="5.715" size="1.778" layer="95">&gt;NAME</text>
<text x="-6.35" y="-5.08" size="1.778" layer="96">&gt;VALUE</text>
<pin name="1" x="-2.54" y="2.54" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="2" x="-2.54" y="0" visible="pad" length="short" direction="pas" function="dot"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="PINHD-1X24" urn="urn:adsk.eagle:component:22528/4" prefix="JP" uservalue="yes" library_version="3">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<gates>
<gate name="A" symbol="PINHD24" x="0" y="0"/>
</gates>
<devices>
<device name="" package="1X24">
<connects>
<connect gate="A" pin="1" pad="1"/>
<connect gate="A" pin="10" pad="10"/>
<connect gate="A" pin="11" pad="11"/>
<connect gate="A" pin="12" pad="12"/>
<connect gate="A" pin="13" pad="13"/>
<connect gate="A" pin="14" pad="14"/>
<connect gate="A" pin="15" pad="15"/>
<connect gate="A" pin="16" pad="16"/>
<connect gate="A" pin="17" pad="17"/>
<connect gate="A" pin="18" pad="18"/>
<connect gate="A" pin="19" pad="19"/>
<connect gate="A" pin="2" pad="2"/>
<connect gate="A" pin="20" pad="20"/>
<connect gate="A" pin="21" pad="21"/>
<connect gate="A" pin="22" pad="22"/>
<connect gate="A" pin="23" pad="23"/>
<connect gate="A" pin="24" pad="24"/>
<connect gate="A" pin="3" pad="3"/>
<connect gate="A" pin="4" pad="4"/>
<connect gate="A" pin="5" pad="5"/>
<connect gate="A" pin="6" pad="6"/>
<connect gate="A" pin="7" pad="7"/>
<connect gate="A" pin="8" pad="8"/>
<connect gate="A" pin="9" pad="9"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:22448/2"/>
</package3dinstances>
<technologies>
<technology name=""/>
</technologies>
</device>
<device name="/90" package="1X24/90">
<connects>
<connect gate="A" pin="1" pad="1"/>
<connect gate="A" pin="10" pad="10"/>
<connect gate="A" pin="11" pad="11"/>
<connect gate="A" pin="12" pad="12"/>
<connect gate="A" pin="13" pad="13"/>
<connect gate="A" pin="14" pad="14"/>
<connect gate="A" pin="15" pad="15"/>
<connect gate="A" pin="16" pad="16"/>
<connect gate="A" pin="17" pad="17"/>
<connect gate="A" pin="18" pad="18"/>
<connect gate="A" pin="19" pad="19"/>
<connect gate="A" pin="2" pad="2"/>
<connect gate="A" pin="20" pad="20"/>
<connect gate="A" pin="21" pad="21"/>
<connect gate="A" pin="22" pad="22"/>
<connect gate="A" pin="23" pad="23"/>
<connect gate="A" pin="24" pad="24"/>
<connect gate="A" pin="3" pad="3"/>
<connect gate="A" pin="4" pad="4"/>
<connect gate="A" pin="5" pad="5"/>
<connect gate="A" pin="6" pad="6"/>
<connect gate="A" pin="7" pad="7"/>
<connect gate="A" pin="8" pad="8"/>
<connect gate="A" pin="9" pad="9"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:22449/2"/>
</package3dinstances>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="PINHD-1X6" urn="urn:adsk.eagle:component:22533/3" prefix="JP" uservalue="yes" library_version="3">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<gates>
<gate name="A" symbol="PINHD6" x="0" y="-2.54"/>
</gates>
<devices>
<device name="" package="1X06">
<connects>
<connect gate="A" pin="1" pad="1"/>
<connect gate="A" pin="2" pad="2"/>
<connect gate="A" pin="3" pad="3"/>
<connect gate="A" pin="4" pad="4"/>
<connect gate="A" pin="5" pad="5"/>
<connect gate="A" pin="6" pad="6"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:22472/2"/>
</package3dinstances>
<technologies>
<technology name=""/>
</technologies>
</device>
<device name="/90" package="1X06/90">
<connects>
<connect gate="A" pin="1" pad="1"/>
<connect gate="A" pin="2" pad="2"/>
<connect gate="A" pin="3" pad="3"/>
<connect gate="A" pin="4" pad="4"/>
<connect gate="A" pin="5" pad="5"/>
<connect gate="A" pin="6" pad="6"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:22475/2"/>
</package3dinstances>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="PINHD-1X2" urn="urn:adsk.eagle:component:22516/3" prefix="JP" uservalue="yes" library_version="3">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<gates>
<gate name="G$1" symbol="PINHD2" x="0" y="0"/>
</gates>
<devices>
<device name="" package="1X02">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:22435/2"/>
</package3dinstances>
<technologies>
<technology name=""/>
</technologies>
</device>
<device name="/90" package="1X02/90">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="2" pad="2"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:22437/2"/>
</package3dinstances>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="con-thomas-betts" urn="urn:adsk.eagle:library:191">
<description>&lt;b&gt;Thomas &amp; Betts Connectors&lt;/b&gt;&lt;p&gt;
Based on Thomas &amp; Betts Catalog &lt;i&gt;Electronioc Interconnects European Edition 1998&lt;/i&gt;.&lt;p&gt;
Created 10.06.1999&lt;br&gt;
Packages changed/corrected 22.02.2006 librarian@cadsoft.de&lt;br&gt;
&lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
<package name="H2M25RA" urn="urn:adsk.eagle:footprint:10512/1" library_version="1">
<description>&lt;b&gt;THOMAS&amp;BETTS&lt;/b&gt; H2M25RA29A</description>
<wire x1="-19.5326" y1="-15.621" x2="-19.5326" y2="-9.779" width="0.254" layer="21"/>
<wire x1="-19.5326" y1="-9.779" x2="-26.3652" y2="-9.779" width="0.254" layer="21"/>
<wire x1="-26.3652" y1="-9.779" x2="-26.3652" y2="8.255" width="0.254" layer="21"/>
<wire x1="-18.3388" y1="8.255" x2="18.3388" y2="8.255" width="0.254" layer="51"/>
<wire x1="26.3652" y1="8.255" x2="26.3652" y2="-9.779" width="0.254" layer="21"/>
<wire x1="26.3652" y1="-9.779" x2="19.5326" y2="-9.779" width="0.254" layer="21"/>
<wire x1="19.5326" y1="-9.779" x2="19.5326" y2="-15.621" width="0.254" layer="21"/>
<wire x1="19.5326" y1="-15.621" x2="-19.5326" y2="-15.621" width="0.254" layer="21"/>
<wire x1="-19.5326" y1="-9.779" x2="19.5326" y2="-9.779" width="0.254" layer="21"/>
<wire x1="-26.3652" y1="8.255" x2="-18.3642" y2="8.255" width="0.254" layer="21"/>
<wire x1="26.3652" y1="8.255" x2="18.3642" y2="8.255" width="0.254" layer="21"/>
<wire x1="-26.3652" y1="-6.858" x2="26.3652" y2="-6.858" width="0.254" layer="21"/>
<pad name="1" x="-16.6116" y="7.9248" drill="1.0922"/>
<pad name="2" x="-13.843" y="7.9248" drill="1.0922"/>
<pad name="3" x="-11.0744" y="7.9248" drill="1.0922"/>
<pad name="4" x="-8.3058" y="7.9248" drill="1.0922"/>
<pad name="5" x="-5.5372" y="7.9248" drill="1.0922"/>
<pad name="6" x="-2.7686" y="7.9248" drill="1.0922"/>
<pad name="7" x="0" y="7.9248" drill="1.0922"/>
<pad name="8" x="2.7686" y="7.9248" drill="1.0922"/>
<pad name="9" x="5.5372" y="7.9248" drill="1.0922"/>
<pad name="10" x="8.3058" y="7.9248" drill="1.0922"/>
<pad name="11" x="11.0744" y="7.9248" drill="1.0922"/>
<pad name="12" x="13.843" y="7.9248" drill="1.0922"/>
<pad name="13" x="16.6116" y="7.9248" drill="1.0922"/>
<pad name="14" x="-15.2273" y="5.08" drill="1.0922"/>
<pad name="15" x="-12.4587" y="5.08" drill="1.0922"/>
<pad name="16" x="-9.6901" y="5.08" drill="1.0922"/>
<pad name="17" x="-6.9215" y="5.08" drill="1.0922"/>
<pad name="18" x="-4.1529" y="5.08" drill="1.0922"/>
<pad name="19" x="-1.3843" y="5.08" drill="1.0922"/>
<pad name="20" x="1.3843" y="5.08" drill="1.0922"/>
<pad name="21" x="4.1529" y="5.08" drill="1.0922"/>
<pad name="22" x="6.9215" y="5.08" drill="1.0922"/>
<pad name="23" x="9.6901" y="5.08" drill="1.0922"/>
<pad name="24" x="12.4587" y="5.08" drill="1.0922"/>
<pad name="25" x="15.2273" y="5.08" drill="1.0922"/>
<text x="-17.145" y="10.16" size="1.27" layer="25">&gt;NAME</text>
<text x="-17.78" y="1.27" size="1.27" layer="27">&gt;VALUE</text>
<hole x="-23.5204" y="-1.905" drill="3.048"/>
<hole x="23.5204" y="-1.905" drill="3.048"/>
</package>
<package name="H2M25ST" urn="urn:adsk.eagle:footprint:10513/1" library_version="1">
<description>&lt;b&gt;THOMAS&amp;BETTS&lt;/b&gt; H2M25ST29x</description>
<wire x1="17.0942" y1="-3.9116" x2="-17.0942" y2="-3.9116" width="0.254" layer="21"/>
<wire x1="18.1102" y1="3.9116" x2="-18.1102" y2="3.9116" width="0.254" layer="21"/>
<wire x1="-17.9832" y1="-3.302" x2="-19.0246" y2="2.5908" width="0.254" layer="21"/>
<wire x1="-19.0246" y1="2.5908" x2="-18.1102" y2="3.9116" width="0.254" layer="21" curve="-107.683629"/>
<wire x1="-17.9832" y1="-3.302" x2="-17.0942" y2="-3.9116" width="0.254" layer="21" curve="68.921633"/>
<wire x1="17.9832" y1="-3.302" x2="19.0246" y2="2.5908" width="0.254" layer="21"/>
<wire x1="18.1102" y1="3.9116" x2="19.0246" y2="2.5908" width="0.254" layer="21" curve="-107.683629"/>
<wire x1="17.0942" y1="-3.9116" x2="17.9832" y2="-3.302" width="0.254" layer="21" curve="68.921633"/>
<wire x1="26.3652" y1="4.6228" x2="26.3652" y2="-4.6228" width="0.254" layer="21"/>
<wire x1="25.8572" y1="-5.1308" x2="-25.8826" y2="-5.1308" width="0.254" layer="21"/>
<wire x1="-26.3652" y1="-4.6482" x2="-26.3652" y2="4.6228" width="0.254" layer="21"/>
<wire x1="-25.8572" y1="5.1308" x2="25.8572" y2="5.1308" width="0.254" layer="21"/>
<wire x1="25.8572" y1="5.1308" x2="26.3652" y2="4.6228" width="0.254" layer="21" curve="-90"/>
<wire x1="-26.3652" y1="4.6228" x2="-25.8572" y2="5.1308" width="0.254" layer="21" curve="-90"/>
<wire x1="-26.3652" y1="-4.6228" x2="-25.8572" y2="-5.1308" width="0.254" layer="21" curve="90"/>
<wire x1="25.8572" y1="-5.1308" x2="26.3652" y2="-4.6228" width="0.254" layer="21" curve="90"/>
<pad name="1" x="-16.6116" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="2" x="-13.843" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="3" x="-11.0744" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="4" x="-8.3058" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="5" x="-5.5372" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="6" x="-2.7686" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="7" x="0" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="8" x="2.7686" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="9" x="5.5372" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="10" x="8.3058" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="11" x="11.0744" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="12" x="13.843" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="13" x="16.6116" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="14" x="-15.2273" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="15" x="-12.4587" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="16" x="-9.6901" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="17" x="-6.9215" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="18" x="-4.1529" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="19" x="-1.3843" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="20" x="1.3843" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="21" x="4.1529" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="22" x="6.9215" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="23" x="9.6901" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="24" x="12.4587" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="25" x="15.2273" y="-1.4224" drill="1.0922" rot="R180"/>
<text x="-24.13" y="5.715" size="1.27" layer="25">&gt;NAME</text>
<text x="-15.875" y="5.715" size="1.27" layer="27">&gt;VALUE</text>
<hole x="-23.5204" y="0" drill="3.048"/>
<hole x="23.5204" y="0" drill="3.048"/>
</package>
<package name="H2R25RA" urn="urn:adsk.eagle:footprint:10514/1" library_version="1">
<description>&lt;b&gt;THOMAS&amp;BETTS&lt;/b&gt; H2R25RA29A</description>
<wire x1="-19.5326" y1="-15.621" x2="-19.5326" y2="-9.779" width="0.254" layer="21"/>
<wire x1="-19.5326" y1="-9.779" x2="-26.3652" y2="-9.779" width="0.254" layer="21"/>
<wire x1="-26.3652" y1="-9.779" x2="-26.3652" y2="8.255" width="0.254" layer="21"/>
<wire x1="-18.3388" y1="8.255" x2="18.3388" y2="8.255" width="0.254" layer="51"/>
<wire x1="26.3652" y1="8.255" x2="26.3652" y2="-9.779" width="0.254" layer="21"/>
<wire x1="26.3652" y1="-9.779" x2="19.5326" y2="-9.779" width="0.254" layer="21"/>
<wire x1="19.5326" y1="-9.779" x2="19.5326" y2="-15.621" width="0.254" layer="21"/>
<wire x1="19.5326" y1="-15.621" x2="-19.5326" y2="-15.621" width="0.254" layer="21"/>
<wire x1="-19.5326" y1="-9.779" x2="19.5326" y2="-9.779" width="0.254" layer="21"/>
<wire x1="-26.3652" y1="8.255" x2="-18.3642" y2="8.255" width="0.254" layer="21"/>
<wire x1="26.3652" y1="8.255" x2="18.3642" y2="8.255" width="0.254" layer="21"/>
<wire x1="-26.3652" y1="-6.858" x2="26.3652" y2="-6.858" width="0.254" layer="21"/>
<pad name="1" x="16.6116" y="7.9248" drill="1.0922"/>
<pad name="2" x="13.843" y="7.9248" drill="1.0922"/>
<pad name="3" x="11.0744" y="7.9248" drill="1.0922"/>
<pad name="4" x="8.3058" y="7.9248" drill="1.0922"/>
<pad name="5" x="5.5372" y="7.9248" drill="1.0922"/>
<pad name="6" x="2.7686" y="7.9248" drill="1.0922"/>
<pad name="7" x="0" y="7.9248" drill="1.0922"/>
<pad name="8" x="-2.7686" y="7.9248" drill="1.0922"/>
<pad name="9" x="-5.5372" y="7.9248" drill="1.0922"/>
<pad name="10" x="-8.3058" y="7.9248" drill="1.0922"/>
<pad name="11" x="-11.0744" y="7.9248" drill="1.0922"/>
<pad name="12" x="-13.843" y="7.9248" drill="1.0922"/>
<pad name="13" x="-16.6116" y="7.9248" drill="1.0922"/>
<pad name="14" x="15.2273" y="5.08" drill="1.0922"/>
<pad name="15" x="12.4587" y="5.08" drill="1.0922"/>
<pad name="16" x="9.6901" y="5.08" drill="1.0922"/>
<pad name="17" x="6.9215" y="5.08" drill="1.0922"/>
<pad name="18" x="4.1529" y="5.08" drill="1.0922"/>
<pad name="19" x="1.3843" y="5.08" drill="1.0922"/>
<pad name="20" x="-1.3843" y="5.08" drill="1.0922"/>
<pad name="21" x="-4.1529" y="5.08" drill="1.0922"/>
<pad name="22" x="-6.9215" y="5.08" drill="1.0922"/>
<pad name="23" x="-9.6901" y="5.08" drill="1.0922"/>
<pad name="24" x="-12.4587" y="5.08" drill="1.0922"/>
<pad name="25" x="-15.2273" y="5.08" drill="1.0922"/>
<text x="-16.51" y="9.525" size="1.27" layer="25">&gt;NAME</text>
<text x="-13.335" y="0.635" size="1.27" layer="27">&gt;VALUE</text>
<hole x="-23.5204" y="-1.905" drill="3.048"/>
<hole x="23.5204" y="-1.905" drill="3.048"/>
</package>
<package name="H2R25ST" urn="urn:adsk.eagle:footprint:10515/1" library_version="1">
<description>&lt;b&gt;THOMAS&amp;BETTS&lt;/b&gt; H2R25ST29x</description>
<wire x1="17.0942" y1="-3.9116" x2="-17.0942" y2="-3.9116" width="0.254" layer="21"/>
<wire x1="18.1102" y1="3.9116" x2="-18.1102" y2="3.9116" width="0.254" layer="21"/>
<wire x1="-17.9832" y1="-3.302" x2="-19.0246" y2="2.5908" width="0.254" layer="21"/>
<wire x1="-19.0246" y1="2.5908" x2="-18.1102" y2="3.9116" width="0.254" layer="21" curve="-107.683629"/>
<wire x1="-17.9832" y1="-3.302" x2="-17.0942" y2="-3.9116" width="0.254" layer="21" curve="68.921633"/>
<wire x1="17.9832" y1="-3.302" x2="19.0246" y2="2.5908" width="0.254" layer="21"/>
<wire x1="18.1102" y1="3.9116" x2="19.0246" y2="2.5908" width="0.254" layer="21" curve="-107.683629"/>
<wire x1="17.0942" y1="-3.9116" x2="17.9832" y2="-3.302" width="0.254" layer="21" curve="68.921633"/>
<wire x1="26.3652" y1="4.6228" x2="26.3652" y2="-4.6228" width="0.254" layer="21"/>
<wire x1="25.8572" y1="-5.1308" x2="-25.8826" y2="-5.1308" width="0.254" layer="21"/>
<wire x1="-26.3652" y1="-4.6482" x2="-26.3652" y2="4.6228" width="0.254" layer="21"/>
<wire x1="-25.8572" y1="5.1308" x2="25.8572" y2="5.1308" width="0.254" layer="21"/>
<wire x1="25.8572" y1="5.1308" x2="26.3652" y2="4.6228" width="0.254" layer="21" curve="-90"/>
<wire x1="-26.3652" y1="4.6228" x2="-25.8572" y2="5.1308" width="0.254" layer="21" curve="-90"/>
<wire x1="-26.3652" y1="-4.6228" x2="-25.8572" y2="-5.1308" width="0.254" layer="21" curve="90"/>
<wire x1="25.8572" y1="-5.1308" x2="26.3652" y2="-4.6228" width="0.254" layer="21" curve="90"/>
<pad name="1" x="16.6116" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="2" x="13.843" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="3" x="11.0744" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="4" x="8.3058" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="5" x="5.5372" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="6" x="2.7686" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="7" x="0" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="8" x="-2.7686" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="9" x="-5.5372" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="10" x="-8.3058" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="11" x="-11.0744" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="12" x="-13.843" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="13" x="-16.6116" y="1.4224" drill="1.0922" rot="R180"/>
<pad name="14" x="15.2273" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="15" x="12.4587" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="16" x="9.6901" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="17" x="6.9215" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="18" x="4.1529" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="19" x="1.3843" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="20" x="-1.3843" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="21" x="-4.1529" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="22" x="-6.9215" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="23" x="-9.6901" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="24" x="-12.4587" y="-1.4224" drill="1.0922" rot="R180"/>
<pad name="25" x="-15.2273" y="-1.4224" drill="1.0922" rot="R180"/>
<text x="-22.86" y="5.715" size="1.27" layer="25">&gt;NAME</text>
<text x="-14.605" y="5.715" size="1.27" layer="27">&gt;VALUE</text>
<hole x="-23.5204" y="0" drill="3.048"/>
<hole x="23.5204" y="0" drill="3.048"/>
</package>
<package name="H3M25RA" urn="urn:adsk.eagle:footprint:10516/1" library_version="1">
<description>&lt;b&gt;THOMAS&amp;BETTS&lt;/b&gt; H3M25RA29A</description>
<wire x1="-19.5326" y1="-15.4813" x2="-19.5326" y2="-9.3599" width="0.254" layer="21"/>
<wire x1="-19.5326" y1="-9.3599" x2="-26.3652" y2="-9.3599" width="0.254" layer="21"/>
<wire x1="-26.3652" y1="-9.3599" x2="-26.3652" y2="3.9751" width="0.254" layer="21"/>
<wire x1="26.3652" y1="3.9497" x2="26.3652" y2="-9.3599" width="0.254" layer="21"/>
<wire x1="26.3652" y1="-9.3599" x2="19.5326" y2="-9.3599" width="0.254" layer="21"/>
<wire x1="19.5326" y1="-9.3599" x2="19.5326" y2="-15.4813" width="0.254" layer="21"/>
<wire x1="19.5326" y1="-15.4813" x2="-19.5326" y2="-15.4813" width="0.254" layer="21"/>
<wire x1="-19.5326" y1="-9.3599" x2="19.5326" y2="-9.3599" width="0.254" layer="21"/>
<wire x1="-26.3652" y1="3.9751" x2="-18.9992" y2="3.9751" width="0.254" layer="21"/>
<wire x1="-18.9992" y1="3.9751" x2="-18.9992" y2="-6.2992" width="0.254" layer="21"/>
<wire x1="26.3652" y1="3.9497" x2="18.9992" y2="3.9497" width="0.254" layer="21"/>
<wire x1="18.9992" y1="3.9497" x2="18.9992" y2="-6.2992" width="0.254" layer="21"/>
<wire x1="-26.3652" y1="-6.4389" x2="26.3652" y2="-6.4389" width="0.254" layer="21"/>
<pad name="1" x="-16.6116" y="1.4224" drill="1.0922"/>
<pad name="2" x="-13.843" y="1.4224" drill="1.0922"/>
<pad name="3" x="-11.0744" y="1.4224" drill="1.0922"/>
<pad name="4" x="-8.3058" y="1.4224" drill="1.0922"/>
<pad name="5" x="-5.5372" y="1.4224" drill="1.0922"/>
<pad name="6" x="-2.7686" y="1.4224" drill="1.0922"/>
<pad name="7" x="0" y="1.4224" drill="1.0922"/>
<pad name="8" x="2.7686" y="1.4224" drill="1.0922"/>
<pad name="9" x="5.5372" y="1.4224" drill="1.0922"/>
<pad name="10" x="8.3058" y="1.4224" drill="1.0922"/>
<pad name="11" x="11.0744" y="1.4224" drill="1.0922"/>
<pad name="12" x="13.843" y="1.4224" drill="1.0922"/>
<pad name="13" x="16.6116" y="1.4224" drill="1.0922"/>
<pad name="14" x="-15.2273" y="-1.4224" drill="1.0922"/>
<pad name="15" x="-12.4587" y="-1.4224" drill="1.0922"/>
<pad name="16" x="-9.6901" y="-1.4224" drill="1.0922"/>
<pad name="17" x="-6.9215" y="-1.4224" drill="1.0922"/>
<pad name="18" x="-4.1529" y="-1.4224" drill="1.0922"/>
<pad name="19" x="-1.3843" y="-1.4224" drill="1.0922"/>
<pad name="20" x="1.3843" y="-1.4224" drill="1.0922"/>
<pad name="21" x="4.1529" y="-1.4224" drill="1.0922"/>
<pad name="22" x="6.9215" y="-1.4224" drill="1.0922"/>
<pad name="23" x="9.6901" y="-1.4224" drill="1.0922"/>
<pad name="24" x="12.4587" y="-1.4224" drill="1.0922"/>
<pad name="25" x="15.2273" y="-1.4224" drill="1.0922"/>
<text x="-17.145" y="3.175" size="1.27" layer="25">&gt;NAME</text>
<text x="-19.05" y="-8.255" size="1.27" layer="27">&gt;VALUE</text>
<hole x="-23.5204" y="0" drill="3.048"/>
<hole x="23.5204" y="0" drill="3.048"/>
</package>
<package name="H5M25RA" urn="urn:adsk.eagle:footprint:10517/1" library_version="1">
<description>&lt;b&gt;THOMAS&amp;BETTS&lt;/b&gt; H5M25RA29A</description>
<wire x1="-19.5326" y1="-15.4813" x2="-19.5326" y2="-9.3599" width="0.254" layer="21"/>
<wire x1="-19.5326" y1="-9.3599" x2="-26.3652" y2="-9.3599" width="0.254" layer="21"/>
<wire x1="-26.3652" y1="-9.3599" x2="-26.3652" y2="3.3401" width="0.254" layer="21"/>
<wire x1="26.3652" y1="3.3147" x2="26.3652" y2="-9.3599" width="0.254" layer="21"/>
<wire x1="26.3652" y1="-9.3599" x2="19.5326" y2="-9.3599" width="0.254" layer="21"/>
<wire x1="19.5326" y1="-9.3599" x2="19.5326" y2="-15.4813" width="0.254" layer="21"/>
<wire x1="19.5326" y1="-15.4813" x2="-19.5326" y2="-15.4813" width="0.254" layer="21"/>
<wire x1="-19.5326" y1="-9.3599" x2="19.5326" y2="-9.3599" width="0.254" layer="21"/>
<wire x1="-26.3652" y1="3.3401" x2="-18.9992" y2="3.3401" width="0.254" layer="21"/>
<wire x1="-18.9992" y1="3.3401" x2="-18.9992" y2="-6.2992" width="0.254" layer="21"/>
<wire x1="26.3652" y1="3.3147" x2="18.9992" y2="3.3147" width="0.254" layer="21"/>
<wire x1="18.9992" y1="3.3147" x2="18.9992" y2="-6.2992" width="0.254" layer="21"/>
<wire x1="-26.3652" y1="-6.4389" x2="26.3652" y2="-6.4389" width="0.254" layer="21"/>
<pad name="1" x="-16.6116" y="1.4224" drill="1.0922"/>
<pad name="2" x="-13.843" y="1.4224" drill="1.0922"/>
<pad name="3" x="-11.0744" y="1.4224" drill="1.0922"/>
<pad name="4" x="-8.3058" y="1.4224" drill="1.0922"/>
<pad name="5" x="-5.5372" y="1.4224" drill="1.0922"/>
<pad name="6" x="-2.7686" y="1.4224" drill="1.0922"/>
<pad name="7" x="0" y="1.4224" drill="1.0922"/>
<pad name="8" x="2.7686" y="1.4224" drill="1.0922"/>
<pad name="9" x="5.5372" y="1.4224" drill="1.0922"/>
<pad name="10" x="8.3058" y="1.4224" drill="1.0922"/>
<pad name="11" x="11.0744" y="1.4224" drill="1.0922"/>
<pad name="12" x="13.843" y="1.4224" drill="1.0922"/>
<pad name="13" x="16.6116" y="1.4224" drill="1.0922"/>
<pad name="14" x="-15.2273" y="-1.4224" drill="1.0922"/>
<pad name="15" x="-12.4587" y="-1.4224" drill="1.0922"/>
<pad name="16" x="-9.6901" y="-1.4224" drill="1.0922"/>
<pad name="17" x="-6.9215" y="-1.4224" drill="1.0922"/>
<pad name="18" x="-4.1529" y="-1.4224" drill="1.0922"/>
<pad name="19" x="-1.3843" y="-1.4224" drill="1.0922"/>
<pad name="20" x="1.3843" y="-1.4224" drill="1.0922"/>
<pad name="21" x="4.1529" y="-1.4224" drill="1.0922"/>
<pad name="22" x="6.9215" y="-1.4224" drill="1.0922"/>
<pad name="23" x="9.6901" y="-1.4224" drill="1.0922"/>
<pad name="24" x="12.4587" y="-1.4224" drill="1.0922"/>
<pad name="25" x="15.2273" y="-1.4224" drill="1.0922"/>
<text x="-16.51" y="3.175" size="1.27" layer="25">&gt;NAME</text>
<text x="-19.685" y="-8.255" size="1.27" layer="27">&gt;VALUE</text>
<hole x="-23.5204" y="0" drill="3.048"/>
<hole x="23.5204" y="0" drill="3.048"/>
</package>
<package name="H5R25RA" urn="urn:adsk.eagle:footprint:10518/1" library_version="1">
<description>&lt;b&gt;THOMAS&amp;BETTS&lt;/b&gt; H5R25RA29A</description>
<wire x1="-19.5326" y1="-15.4813" x2="-19.5326" y2="-9.3599" width="0.254" layer="21"/>
<wire x1="-19.5326" y1="-9.3599" x2="-26.3652" y2="-9.3599" width="0.254" layer="21"/>
<wire x1="-26.3652" y1="-9.3599" x2="-26.3652" y2="3.3401" width="0.254" layer="21"/>
<wire x1="26.3652" y1="3.3147" x2="26.3652" y2="-9.3599" width="0.254" layer="21"/>
<wire x1="26.3652" y1="-9.3599" x2="19.5326" y2="-9.3599" width="0.254" layer="21"/>
<wire x1="19.5326" y1="-9.3599" x2="19.5326" y2="-15.4813" width="0.254" layer="21"/>
<wire x1="19.5326" y1="-15.4813" x2="-19.5326" y2="-15.4813" width="0.254" layer="21"/>
<wire x1="-19.5326" y1="-9.3599" x2="19.5326" y2="-9.3599" width="0.254" layer="21"/>
<wire x1="-26.3652" y1="3.3401" x2="-18.9992" y2="3.3401" width="0.254" layer="21"/>
<wire x1="-18.9992" y1="3.3401" x2="-18.9992" y2="-6.2992" width="0.254" layer="21"/>
<wire x1="26.3652" y1="3.3147" x2="18.9992" y2="3.3147" width="0.254" layer="21"/>
<wire x1="18.9992" y1="3.3147" x2="18.9992" y2="-6.2992" width="0.254" layer="21"/>
<wire x1="-26.3652" y1="-6.4389" x2="26.3652" y2="-6.4389" width="0.254" layer="21"/>
<pad name="1" x="16.6116" y="1.4224" drill="1.0922"/>
<pad name="2" x="13.843" y="1.4224" drill="1.0922"/>
<pad name="3" x="11.0744" y="1.4224" drill="1.0922"/>
<pad name="4" x="8.3058" y="1.4224" drill="1.0922"/>
<pad name="5" x="5.5372" y="1.4224" drill="1.0922"/>
<pad name="6" x="2.7686" y="1.4224" drill="1.0922"/>
<pad name="7" x="0" y="1.4224" drill="1.0922"/>
<pad name="8" x="-2.7686" y="1.4224" drill="1.0922"/>
<pad name="9" x="-5.5372" y="1.4224" drill="1.0922"/>
<pad name="10" x="-8.3058" y="1.4224" drill="1.0922"/>
<pad name="11" x="-11.0744" y="1.4224" drill="1.0922"/>
<pad name="12" x="-13.843" y="1.4224" drill="1.0922"/>
<pad name="13" x="-16.6116" y="1.4224" drill="1.0922"/>
<pad name="14" x="15.2273" y="-1.4224" drill="1.0922"/>
<pad name="15" x="12.4587" y="-1.4224" drill="1.0922"/>
<pad name="16" x="9.6901" y="-1.4224" drill="1.0922"/>
<pad name="17" x="6.9215" y="-1.4224" drill="1.0922"/>
<pad name="18" x="4.1529" y="-1.4224" drill="1.0922"/>
<pad name="19" x="1.3843" y="-1.4224" drill="1.0922"/>
<pad name="20" x="-1.3843" y="-1.4224" drill="1.0922"/>
<pad name="21" x="-4.1529" y="-1.4224" drill="1.0922"/>
<pad name="22" x="-6.9215" y="-1.4224" drill="1.0922"/>
<pad name="23" x="-9.6901" y="-1.4224" drill="1.0922"/>
<pad name="24" x="-12.4587" y="-1.4224" drill="1.0922"/>
<pad name="25" x="-15.2273" y="-1.4224" drill="1.0922"/>
<text x="-16.51" y="2.54" size="1.27" layer="25">&gt;NAME</text>
<text x="-19.685" y="-8.89" size="1.27" layer="27">&gt;VALUE</text>
<hole x="-23.5204" y="0" drill="3.048"/>
<hole x="23.5204" y="0" drill="3.048"/>
</package>
</packages>
<packages3d>
<package3d name="H2M25RA" urn="urn:adsk.eagle:package:10570/1" type="box" library_version="1">
<description>THOMAS&amp;BETTS H2M25RA29A</description>
<packageinstances>
<packageinstance name="H2M25RA"/>
</packageinstances>
</package3d>
<package3d name="H2M25ST" urn="urn:adsk.eagle:package:10572/1" type="box" library_version="1">
<description>THOMAS&amp;BETTS H2M25ST29x</description>
<packageinstances>
<packageinstance name="H2M25ST"/>
</packageinstances>
</package3d>
<package3d name="H2R25RA" urn="urn:adsk.eagle:package:10573/1" type="box" library_version="1">
<description>THOMAS&amp;BETTS H2R25RA29A</description>
<packageinstances>
<packageinstance name="H2R25RA"/>
</packageinstances>
</package3d>
<package3d name="H2R25ST" urn="urn:adsk.eagle:package:10571/1" type="box" library_version="1">
<description>THOMAS&amp;BETTS H2R25ST29x</description>
<packageinstances>
<packageinstance name="H2R25ST"/>
</packageinstances>
</package3d>
<package3d name="H3M25RA" urn="urn:adsk.eagle:package:10592/1" type="box" library_version="1">
<description>THOMAS&amp;BETTS H3M25RA29A</description>
<packageinstances>
<packageinstance name="H3M25RA"/>
</packageinstances>
</package3d>
<package3d name="H5M25RA" urn="urn:adsk.eagle:package:10574/1" type="box" library_version="1">
<description>THOMAS&amp;BETTS H5M25RA29A</description>
<packageinstances>
<packageinstance name="H5M25RA"/>
</packageinstances>
</package3d>
<package3d name="H5R25RA" urn="urn:adsk.eagle:package:10577/1" type="box" library_version="1">
<description>THOMAS&amp;BETTS H5R25RA29A</description>
<packageinstances>
<packageinstance name="H5R25RA"/>
</packageinstances>
</package3d>
</packages3d>
<symbols>
<symbol name="FV" urn="urn:adsk.eagle:symbol:10475/1" library_version="1">
<wire x1="0.889" y1="0.889" x2="0.889" y2="-0.889" width="0.254" layer="94" curve="180" cap="flat"/>
<text x="1.27" y="-0.762" size="1.778" layer="95">&gt;NAME</text>
<text x="-2.54" y="1.397" size="1.778" layer="96">&gt;VALUE</text>
<pin name="F" x="-2.54" y="0" visible="off" length="short" direction="pas"/>
</symbol>
<symbol name="F" urn="urn:adsk.eagle:symbol:10474/1" library_version="1">
<wire x1="0.889" y1="0.889" x2="0.889" y2="-0.889" width="0.254" layer="94" curve="180" cap="flat"/>
<text x="1.27" y="-0.762" size="1.778" layer="95">&gt;NAME</text>
<pin name="F" x="-2.54" y="0" visible="off" length="short" direction="pas"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="D-SUB25-" urn="urn:adsk.eagle:component:10606/1" prefix="X" library_version="1">
<description>&lt;b&gt;D-Subminiatur Connector&lt;/b&gt;&lt;p&gt;
Source: Electronioc Interconnects European Edition 1998</description>
<gates>
<gate name="-1" symbol="FV" x="0" y="30.48" addlevel="always" swaplevel="1"/>
<gate name="-2" symbol="F" x="0" y="27.94" addlevel="always" swaplevel="1"/>
<gate name="-3" symbol="F" x="0" y="25.4" addlevel="always" swaplevel="1"/>
<gate name="-4" symbol="F" x="0" y="22.86" addlevel="always" swaplevel="1"/>
<gate name="-5" symbol="F" x="0" y="20.32" addlevel="always" swaplevel="1"/>
<gate name="-6" symbol="F" x="0" y="17.78" addlevel="always" swaplevel="1"/>
<gate name="-7" symbol="F" x="0" y="15.24" addlevel="always" swaplevel="1"/>
<gate name="-8" symbol="F" x="0" y="12.7" addlevel="always" swaplevel="1"/>
<gate name="-9" symbol="F" x="0" y="10.16" addlevel="always" swaplevel="1"/>
<gate name="-10" symbol="F" x="0" y="7.62" addlevel="always" swaplevel="1"/>
<gate name="-11" symbol="F" x="0" y="5.08" addlevel="always" swaplevel="1"/>
<gate name="-12" symbol="F" x="0" y="2.54" addlevel="always" swaplevel="1"/>
<gate name="-13" symbol="F" x="0" y="0" addlevel="always" swaplevel="1"/>
<gate name="-14" symbol="F" x="0" y="-2.54" addlevel="always" swaplevel="1"/>
<gate name="-15" symbol="F" x="0" y="-5.08" addlevel="always" swaplevel="1"/>
<gate name="-16" symbol="F" x="0" y="-7.62" addlevel="always" swaplevel="1"/>
<gate name="-17" symbol="F" x="0" y="-10.16" addlevel="always" swaplevel="1"/>
<gate name="-18" symbol="F" x="0" y="-12.7" addlevel="always" swaplevel="1"/>
<gate name="-19" symbol="F" x="0" y="-15.24" addlevel="always" swaplevel="1"/>
<gate name="-20" symbol="F" x="0" y="-17.78" addlevel="always" swaplevel="1"/>
<gate name="-21" symbol="F" x="0" y="-20.32" addlevel="always" swaplevel="1"/>
<gate name="-22" symbol="F" x="0" y="-22.86" addlevel="always" swaplevel="1"/>
<gate name="-23" symbol="F" x="0" y="-25.4" addlevel="always" swaplevel="1"/>
<gate name="-24" symbol="F" x="0" y="-27.94" addlevel="always" swaplevel="1"/>
<gate name="-25" symbol="F" x="0" y="-30.48" addlevel="always" swaplevel="1"/>
</gates>
<devices>
<device name="H2M25RA" package="H2M25RA">
<connects>
<connect gate="-1" pin="F" pad="1"/>
<connect gate="-10" pin="F" pad="10"/>
<connect gate="-11" pin="F" pad="11"/>
<connect gate="-12" pin="F" pad="12"/>
<connect gate="-13" pin="F" pad="13"/>
<connect gate="-14" pin="F" pad="14"/>
<connect gate="-15" pin="F" pad="15"/>
<connect gate="-16" pin="F" pad="16"/>
<connect gate="-17" pin="F" pad="17"/>
<connect gate="-18" pin="F" pad="18"/>
<connect gate="-19" pin="F" pad="19"/>
<connect gate="-2" pin="F" pad="2"/>
<connect gate="-20" pin="F" pad="20"/>
<connect gate="-21" pin="F" pad="21"/>
<connect gate="-22" pin="F" pad="22"/>
<connect gate="-23" pin="F" pad="23"/>
<connect gate="-24" pin="F" pad="24"/>
<connect gate="-25" pin="F" pad="25"/>
<connect gate="-3" pin="F" pad="3"/>
<connect gate="-4" pin="F" pad="4"/>
<connect gate="-5" pin="F" pad="5"/>
<connect gate="-6" pin="F" pad="6"/>
<connect gate="-7" pin="F" pad="7"/>
<connect gate="-8" pin="F" pad="8"/>
<connect gate="-9" pin="F" pad="9"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:10570/1"/>
</package3dinstances>
<technologies>
<technology name="">
<attribute name="MF" value="" constant="no"/>
<attribute name="MPN" value="" constant="no"/>
<attribute name="OC_FARNELL" value="unknown" constant="no"/>
<attribute name="OC_NEWARK" value="unknown" constant="no"/>
</technology>
</technologies>
</device>
<device name="H2M25ST" package="H2M25ST">
<connects>
<connect gate="-1" pin="F" pad="1"/>
<connect gate="-10" pin="F" pad="10"/>
<connect gate="-11" pin="F" pad="11"/>
<connect gate="-12" pin="F" pad="12"/>
<connect gate="-13" pin="F" pad="13"/>
<connect gate="-14" pin="F" pad="14"/>
<connect gate="-15" pin="F" pad="15"/>
<connect gate="-16" pin="F" pad="16"/>
<connect gate="-17" pin="F" pad="17"/>
<connect gate="-18" pin="F" pad="18"/>
<connect gate="-19" pin="F" pad="19"/>
<connect gate="-2" pin="F" pad="2"/>
<connect gate="-20" pin="F" pad="20"/>
<connect gate="-21" pin="F" pad="21"/>
<connect gate="-22" pin="F" pad="22"/>
<connect gate="-23" pin="F" pad="23"/>
<connect gate="-24" pin="F" pad="24"/>
<connect gate="-25" pin="F" pad="25"/>
<connect gate="-3" pin="F" pad="3"/>
<connect gate="-4" pin="F" pad="4"/>
<connect gate="-5" pin="F" pad="5"/>
<connect gate="-6" pin="F" pad="6"/>
<connect gate="-7" pin="F" pad="7"/>
<connect gate="-8" pin="F" pad="8"/>
<connect gate="-9" pin="F" pad="9"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:10572/1"/>
</package3dinstances>
<technologies>
<technology name="">
<attribute name="MF" value="" constant="no"/>
<attribute name="MPN" value="" constant="no"/>
<attribute name="OC_FARNELL" value="unknown" constant="no"/>
<attribute name="OC_NEWARK" value="unknown" constant="no"/>
</technology>
</technologies>
</device>
<device name="H2R25RA" package="H2R25RA">
<connects>
<connect gate="-1" pin="F" pad="1"/>
<connect gate="-10" pin="F" pad="10"/>
<connect gate="-11" pin="F" pad="11"/>
<connect gate="-12" pin="F" pad="12"/>
<connect gate="-13" pin="F" pad="13"/>
<connect gate="-14" pin="F" pad="14"/>
<connect gate="-15" pin="F" pad="15"/>
<connect gate="-16" pin="F" pad="16"/>
<connect gate="-17" pin="F" pad="17"/>
<connect gate="-18" pin="F" pad="18"/>
<connect gate="-19" pin="F" pad="19"/>
<connect gate="-2" pin="F" pad="2"/>
<connect gate="-20" pin="F" pad="20"/>
<connect gate="-21" pin="F" pad="21"/>
<connect gate="-22" pin="F" pad="22"/>
<connect gate="-23" pin="F" pad="23"/>
<connect gate="-24" pin="F" pad="24"/>
<connect gate="-25" pin="F" pad="25"/>
<connect gate="-3" pin="F" pad="3"/>
<connect gate="-4" pin="F" pad="4"/>
<connect gate="-5" pin="F" pad="5"/>
<connect gate="-6" pin="F" pad="6"/>
<connect gate="-7" pin="F" pad="7"/>
<connect gate="-8" pin="F" pad="8"/>
<connect gate="-9" pin="F" pad="9"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:10573/1"/>
</package3dinstances>
<technologies>
<technology name="">
<attribute name="MF" value="" constant="no"/>
<attribute name="MPN" value="" constant="no"/>
<attribute name="OC_FARNELL" value="unknown" constant="no"/>
<attribute name="OC_NEWARK" value="unknown" constant="no"/>
</technology>
</technologies>
</device>
<device name="H2R25ST" package="H2R25ST">
<connects>
<connect gate="-1" pin="F" pad="1"/>
<connect gate="-10" pin="F" pad="10"/>
<connect gate="-11" pin="F" pad="11"/>
<connect gate="-12" pin="F" pad="12"/>
<connect gate="-13" pin="F" pad="13"/>
<connect gate="-14" pin="F" pad="14"/>
<connect gate="-15" pin="F" pad="15"/>
<connect gate="-16" pin="F" pad="16"/>
<connect gate="-17" pin="F" pad="17"/>
<connect gate="-18" pin="F" pad="18"/>
<connect gate="-19" pin="F" pad="19"/>
<connect gate="-2" pin="F" pad="2"/>
<connect gate="-20" pin="F" pad="20"/>
<connect gate="-21" pin="F" pad="21"/>
<connect gate="-22" pin="F" pad="22"/>
<connect gate="-23" pin="F" pad="23"/>
<connect gate="-24" pin="F" pad="24"/>
<connect gate="-25" pin="F" pad="25"/>
<connect gate="-3" pin="F" pad="3"/>
<connect gate="-4" pin="F" pad="4"/>
<connect gate="-5" pin="F" pad="5"/>
<connect gate="-6" pin="F" pad="6"/>
<connect gate="-7" pin="F" pad="7"/>
<connect gate="-8" pin="F" pad="8"/>
<connect gate="-9" pin="F" pad="9"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:10571/1"/>
</package3dinstances>
<technologies>
<technology name="">
<attribute name="MF" value="TYCO ELECTRONICS" constant="no"/>
<attribute name="MPN" value="H2R25ST29J" constant="no"/>
<attribute name="OC_FARNELL" value="unknown" constant="no"/>
<attribute name="OC_NEWARK" value="16F4224" constant="no"/>
</technology>
</technologies>
</device>
<device name="H3M25RA" package="H3M25RA">
<connects>
<connect gate="-1" pin="F" pad="1"/>
<connect gate="-10" pin="F" pad="10"/>
<connect gate="-11" pin="F" pad="11"/>
<connect gate="-12" pin="F" pad="12"/>
<connect gate="-13" pin="F" pad="13"/>
<connect gate="-14" pin="F" pad="14"/>
<connect gate="-15" pin="F" pad="15"/>
<connect gate="-16" pin="F" pad="16"/>
<connect gate="-17" pin="F" pad="17"/>
<connect gate="-18" pin="F" pad="18"/>
<connect gate="-19" pin="F" pad="19"/>
<connect gate="-2" pin="F" pad="2"/>
<connect gate="-20" pin="F" pad="20"/>
<connect gate="-21" pin="F" pad="21"/>
<connect gate="-22" pin="F" pad="22"/>
<connect gate="-23" pin="F" pad="23"/>
<connect gate="-24" pin="F" pad="24"/>
<connect gate="-25" pin="F" pad="25"/>
<connect gate="-3" pin="F" pad="3"/>
<connect gate="-4" pin="F" pad="4"/>
<connect gate="-5" pin="F" pad="5"/>
<connect gate="-6" pin="F" pad="6"/>
<connect gate="-7" pin="F" pad="7"/>
<connect gate="-8" pin="F" pad="8"/>
<connect gate="-9" pin="F" pad="9"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:10592/1"/>
</package3dinstances>
<technologies>
<technology name="">
<attribute name="MF" value="" constant="no"/>
<attribute name="MPN" value="" constant="no"/>
<attribute name="OC_FARNELL" value="unknown" constant="no"/>
<attribute name="OC_NEWARK" value="unknown" constant="no"/>
</technology>
</technologies>
</device>
<device name="H5M25RA" package="H5M25RA">
<connects>
<connect gate="-1" pin="F" pad="1"/>
<connect gate="-10" pin="F" pad="10"/>
<connect gate="-11" pin="F" pad="11"/>
<connect gate="-12" pin="F" pad="12"/>
<connect gate="-13" pin="F" pad="13"/>
<connect gate="-14" pin="F" pad="14"/>
<connect gate="-15" pin="F" pad="15"/>
<connect gate="-16" pin="F" pad="16"/>
<connect gate="-17" pin="F" pad="17"/>
<connect gate="-18" pin="F" pad="18"/>
<connect gate="-19" pin="F" pad="19"/>
<connect gate="-2" pin="F" pad="2"/>
<connect gate="-20" pin="F" pad="20"/>
<connect gate="-21" pin="F" pad="21"/>
<connect gate="-22" pin="F" pad="22"/>
<connect gate="-23" pin="F" pad="23"/>
<connect gate="-24" pin="F" pad="24"/>
<connect gate="-25" pin="F" pad="25"/>
<connect gate="-3" pin="F" pad="3"/>
<connect gate="-4" pin="F" pad="4"/>
<connect gate="-5" pin="F" pad="5"/>
<connect gate="-6" pin="F" pad="6"/>
<connect gate="-7" pin="F" pad="7"/>
<connect gate="-8" pin="F" pad="8"/>
<connect gate="-9" pin="F" pad="9"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:10574/1"/>
</package3dinstances>
<technologies>
<technology name="">
<attribute name="MF" value="" constant="no"/>
<attribute name="MPN" value="H5M25RA29CS" constant="no"/>
<attribute name="OC_FARNELL" value="unknown" constant="no"/>
<attribute name="OC_NEWARK" value="93F8324" constant="no"/>
</technology>
</technologies>
</device>
<device name="H5R25RA" package="H5R25RA">
<connects>
<connect gate="-1" pin="F" pad="1"/>
<connect gate="-10" pin="F" pad="10"/>
<connect gate="-11" pin="F" pad="11"/>
<connect gate="-12" pin="F" pad="12"/>
<connect gate="-13" pin="F" pad="13"/>
<connect gate="-14" pin="F" pad="14"/>
<connect gate="-15" pin="F" pad="15"/>
<connect gate="-16" pin="F" pad="16"/>
<connect gate="-17" pin="F" pad="17"/>
<connect gate="-18" pin="F" pad="18"/>
<connect gate="-19" pin="F" pad="19"/>
<connect gate="-2" pin="F" pad="2"/>
<connect gate="-20" pin="F" pad="20"/>
<connect gate="-21" pin="F" pad="21"/>
<connect gate="-22" pin="F" pad="22"/>
<connect gate="-23" pin="F" pad="23"/>
<connect gate="-24" pin="F" pad="24"/>
<connect gate="-25" pin="F" pad="25"/>
<connect gate="-3" pin="F" pad="3"/>
<connect gate="-4" pin="F" pad="4"/>
<connect gate="-5" pin="F" pad="5"/>
<connect gate="-6" pin="F" pad="6"/>
<connect gate="-7" pin="F" pad="7"/>
<connect gate="-8" pin="F" pad="8"/>
<connect gate="-9" pin="F" pad="9"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:10577/1"/>
</package3dinstances>
<technologies>
<technology name="">
<attribute name="MF" value="" constant="no"/>
<attribute name="MPN" value="H5R25RA29CS" constant="no"/>
<attribute name="OC_FARNELL" value="unknown" constant="no"/>
<attribute name="OC_NEWARK" value="93F8340" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="JP1" library="pinhead" library_urn="urn:adsk.eagle:library:325" deviceset="PINHD-1X24" device="" package3d_urn="urn:adsk.eagle:package:22448/2"/>
<part name="JP2" library="pinhead" library_urn="urn:adsk.eagle:library:325" deviceset="PINHD-1X24" device="" package3d_urn="urn:adsk.eagle:package:22448/2"/>
<part name="X1" library="con-thomas-betts" library_urn="urn:adsk.eagle:library:191" deviceset="D-SUB25-" device="H2M25RA" package3d_urn="urn:adsk.eagle:package:10570/1"/>
<part name="SPI1" library="pinhead" library_urn="urn:adsk.eagle:library:325" deviceset="PINHD-1X6" device="" package3d_urn="urn:adsk.eagle:package:22472/2"/>
<part name="SPI2" library="pinhead" library_urn="urn:adsk.eagle:library:325" deviceset="PINHD-1X6" device="" package3d_urn="urn:adsk.eagle:package:22472/2"/>
<part name="JP3" library="pinhead" library_urn="urn:adsk.eagle:library:325" deviceset="PINHD-1X2" device="" package3d_urn="urn:adsk.eagle:package:22435/2"/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="JP1" gate="A" x="10.16" y="53.34"/>
<instance part="JP2" gate="A" x="27.94" y="50.8" rot="R180"/>
<instance part="X1" gate="-1" x="-63.5" y="20.32" rot="R180"/>
<instance part="X1" gate="-2" x="-63.5" y="22.86" rot="R180"/>
<instance part="X1" gate="-3" x="-63.5" y="25.4" rot="R180"/>
<instance part="X1" gate="-4" x="-63.5" y="27.94" rot="R180"/>
<instance part="X1" gate="-5" x="-63.5" y="30.48" rot="R180"/>
<instance part="X1" gate="-6" x="-63.5" y="33.02" rot="R180"/>
<instance part="X1" gate="-7" x="-63.5" y="35.56" rot="R180"/>
<instance part="X1" gate="-8" x="-63.5" y="38.1" rot="R180"/>
<instance part="X1" gate="-9" x="-63.5" y="40.64" rot="R180"/>
<instance part="X1" gate="-10" x="-63.5" y="43.18" rot="R180"/>
<instance part="X1" gate="-11" x="-63.5" y="45.72" rot="R180"/>
<instance part="X1" gate="-12" x="-63.5" y="48.26" rot="R180"/>
<instance part="X1" gate="-13" x="-63.5" y="50.8" rot="R180"/>
<instance part="X1" gate="-14" x="-63.5" y="53.34" rot="R180"/>
<instance part="X1" gate="-15" x="-63.5" y="55.88" rot="R180"/>
<instance part="X1" gate="-16" x="-63.5" y="58.42" rot="R180"/>
<instance part="X1" gate="-17" x="-63.5" y="60.96" rot="R180"/>
<instance part="X1" gate="-18" x="-63.5" y="63.5" rot="R180"/>
<instance part="X1" gate="-19" x="-63.5" y="66.04" rot="R180"/>
<instance part="X1" gate="-20" x="-63.5" y="68.58" rot="R180"/>
<instance part="X1" gate="-21" x="-63.5" y="71.12" rot="R180"/>
<instance part="X1" gate="-22" x="-63.5" y="73.66" rot="R180"/>
<instance part="X1" gate="-23" x="-63.5" y="76.2" rot="R180"/>
<instance part="X1" gate="-24" x="-63.5" y="78.74" rot="R180"/>
<instance part="X1" gate="-25" x="-63.5" y="81.28" rot="R180"/>
<instance part="SPI1" gate="A" x="76.2" y="30.48"/>
<instance part="SPI2" gate="A" x="99.06" y="48.26"/>
<instance part="JP3" gate="G$1" x="-5.08" y="93.98"/>
</instances>
<busses>
</busses>
<nets>
<net name="3V3" class="0">
<segment>
<wire x1="86.36" y1="22.86" x2="30.48" y2="22.86" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="1"/>
<label x="55.88" y="22.86" size="1.778" layer="95"/>
<pinref part="SPI2" gate="A" pin="1"/>
<wire x1="96.52" y1="55.88" x2="86.36" y2="55.88" width="0.1524" layer="91"/>
<wire x1="86.36" y1="55.88" x2="86.36" y2="22.86" width="0.1524" layer="91"/>
</segment>
</net>
<net name="38" class="0">
<segment>
<pinref part="JP1" gate="A" pin="1"/>
<wire x1="7.62" y1="81.28" x2="-22.86" y2="81.28" width="0.1524" layer="91"/>
<label x="-22.86" y="81.28" size="1.778" layer="95"/>
</segment>
</net>
<net name="37" class="0">
<segment>
<wire x1="7.62" y1="78.74" x2="-22.86" y2="78.74" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="2"/>
<label x="-22.86" y="78.74" size="1.778" layer="95"/>
</segment>
</net>
<net name="36" class="0">
<segment>
<wire x1="7.62" y1="76.2" x2="-22.86" y2="76.2" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="3"/>
<label x="-22.86" y="76.2" size="1.778" layer="95"/>
</segment>
</net>
<net name="39" class="0">
<segment>
<wire x1="7.62" y1="73.66" x2="-22.86" y2="73.66" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="4"/>
<label x="-22.86" y="73.66" size="1.778" layer="95"/>
</segment>
</net>
<net name="25" class="0">
<segment>
<wire x1="7.62" y1="71.12" x2="-22.86" y2="71.12" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="5"/>
<label x="-22.86" y="71.12" size="1.778" layer="95"/>
</segment>
</net>
<net name="26" class="0">
<segment>
<wire x1="7.62" y1="68.58" x2="-22.86" y2="68.58" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="6"/>
<label x="-22.86" y="68.58" size="1.778" layer="95"/>
</segment>
</net>
<net name="27" class="0">
<segment>
<wire x1="7.62" y1="66.04" x2="-22.86" y2="66.04" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="7"/>
<label x="-22.86" y="66.04" size="1.778" layer="95"/>
</segment>
</net>
<net name="28" class="0">
<segment>
<wire x1="7.62" y1="63.5" x2="-22.86" y2="63.5" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="8"/>
<label x="-22.86" y="63.5" size="1.778" layer="95"/>
</segment>
<segment>
<wire x1="-60.96" y1="50.8" x2="-30.48" y2="50.8" width="0.1524" layer="91"/>
<label x="-30.48" y="50.8" size="1.778" layer="95" rot="MR0"/>
<pinref part="X1" gate="-13" pin="F"/>
</segment>
</net>
<net name="29" class="0">
<segment>
<wire x1="7.62" y1="60.96" x2="-22.86" y2="60.96" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="9"/>
<label x="-22.86" y="60.96" size="1.778" layer="95"/>
</segment>
<segment>
<wire x1="-60.96" y1="48.26" x2="-30.48" y2="48.26" width="0.1524" layer="91"/>
<label x="-30.48" y="48.26" size="1.778" layer="95" rot="MR0"/>
<pinref part="X1" gate="-12" pin="F"/>
</segment>
</net>
<net name="30" class="0">
<segment>
<wire x1="7.62" y1="58.42" x2="-22.86" y2="58.42" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="10"/>
<label x="-22.86" y="58.42" size="1.778" layer="95"/>
</segment>
<segment>
<wire x1="-60.96" y1="45.72" x2="-30.48" y2="45.72" width="0.1524" layer="91"/>
<label x="-30.48" y="45.72" size="1.778" layer="95" rot="MR0"/>
<pinref part="X1" gate="-11" pin="F"/>
</segment>
</net>
<net name="33" class="0">
<segment>
<wire x1="7.62" y1="55.88" x2="-22.86" y2="55.88" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="11"/>
<label x="-22.86" y="55.88" size="1.778" layer="95"/>
</segment>
<segment>
<wire x1="-60.96" y1="43.18" x2="-30.48" y2="43.18" width="0.1524" layer="91"/>
<label x="-30.48" y="43.18" size="1.778" layer="95" rot="MR0"/>
<pinref part="X1" gate="-10" pin="F"/>
</segment>
</net>
<net name="34" class="0">
<segment>
<wire x1="7.62" y1="53.34" x2="-22.86" y2="53.34" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="12"/>
<label x="-22.86" y="53.34" size="1.778" layer="95"/>
</segment>
<segment>
<wire x1="-60.96" y1="40.64" x2="-30.48" y2="40.64" width="0.1524" layer="91"/>
<label x="-30.48" y="40.64" size="1.778" layer="95" rot="MR0"/>
<pinref part="X1" gate="-9" pin="F"/>
</segment>
</net>
<net name="40" class="0">
<segment>
<wire x1="7.62" y1="50.8" x2="-22.86" y2="50.8" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="13"/>
<label x="-22.86" y="50.8" size="1.778" layer="95"/>
</segment>
<segment>
<wire x1="-60.96" y1="38.1" x2="-30.48" y2="38.1" width="0.1524" layer="91"/>
<label x="-30.48" y="38.1" size="1.778" layer="95" rot="MR0"/>
<pinref part="X1" gate="-8" pin="F"/>
</segment>
</net>
<net name="35" class="0">
<segment>
<wire x1="7.62" y1="48.26" x2="-22.86" y2="48.26" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="14"/>
<label x="-22.86" y="48.26" size="1.778" layer="95"/>
</segment>
<segment>
<wire x1="-60.96" y1="35.56" x2="-30.48" y2="35.56" width="0.1524" layer="91"/>
<label x="-30.48" y="35.56" size="1.778" layer="95" rot="MR0"/>
<pinref part="X1" gate="-7" pin="F"/>
</segment>
</net>
<net name="41" class="0">
<segment>
<wire x1="7.62" y1="45.72" x2="-22.86" y2="45.72" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="15"/>
<label x="-22.86" y="45.72" size="1.778" layer="95"/>
</segment>
<segment>
<wire x1="-60.96" y1="33.02" x2="-30.48" y2="33.02" width="0.1524" layer="91"/>
<label x="-30.48" y="33.02" size="1.778" layer="95" rot="MR0"/>
<pinref part="X1" gate="-6" pin="F"/>
</segment>
</net>
<net name="42" class="0">
<segment>
<wire x1="7.62" y1="43.18" x2="-22.86" y2="43.18" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="16"/>
<label x="-22.86" y="43.18" size="1.778" layer="95"/>
</segment>
<segment>
<wire x1="-60.96" y1="30.48" x2="-30.48" y2="30.48" width="0.1524" layer="91"/>
<label x="-30.48" y="30.48" size="1.778" layer="95" rot="MR0"/>
<pinref part="X1" gate="-5" pin="F"/>
</segment>
</net>
<net name="51" class="0">
<segment>
<wire x1="7.62" y1="40.64" x2="-22.86" y2="40.64" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="17"/>
<label x="-22.86" y="40.64" size="1.778" layer="95"/>
</segment>
<segment>
<wire x1="-60.96" y1="27.94" x2="-30.48" y2="27.94" width="0.1524" layer="91"/>
<label x="-30.48" y="27.94" size="1.778" layer="95" rot="MR0"/>
<pinref part="X1" gate="-4" pin="F"/>
</segment>
</net>
<net name="53" class="0">
<segment>
<wire x1="7.62" y1="38.1" x2="-22.86" y2="38.1" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="18"/>
<label x="-22.86" y="38.1" size="1.778" layer="95"/>
</segment>
<segment>
<wire x1="-60.96" y1="25.4" x2="-30.48" y2="25.4" width="0.1524" layer="91"/>
<label x="-30.48" y="25.4" size="1.778" layer="95" rot="MR0"/>
<pinref part="X1" gate="-3" pin="F"/>
</segment>
</net>
<net name="54" class="0">
<segment>
<wire x1="7.62" y1="35.56" x2="-22.86" y2="35.56" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="19"/>
<label x="-22.86" y="35.56" size="1.778" layer="95"/>
</segment>
<segment>
<wire x1="-60.96" y1="22.86" x2="-30.48" y2="22.86" width="0.1524" layer="91"/>
<label x="-30.48" y="22.86" size="1.778" layer="95" rot="MR0"/>
<pinref part="X1" gate="-2" pin="F"/>
</segment>
</net>
<net name="55" class="0">
<segment>
<wire x1="7.62" y1="33.02" x2="-22.86" y2="33.02" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="20"/>
<label x="-22.86" y="33.02" size="1.778" layer="95"/>
</segment>
<segment>
<wire x1="-60.96" y1="20.32" x2="-30.48" y2="20.32" width="0.1524" layer="91"/>
<label x="-30.48" y="20.32" size="1.778" layer="95" rot="MR0"/>
<pinref part="X1" gate="-1" pin="F"/>
</segment>
</net>
<net name="56" class="0">
<segment>
<wire x1="7.62" y1="30.48" x2="-22.86" y2="30.48" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="21"/>
<label x="-22.86" y="30.48" size="1.778" layer="95"/>
</segment>
<segment>
<wire x1="-60.96" y1="60.96" x2="-30.48" y2="60.96" width="0.1524" layer="91"/>
<label x="-33.02" y="60.96" size="1.778" layer="95" rot="MR0"/>
<pinref part="X1" gate="-17" pin="F"/>
</segment>
</net>
<net name="57" class="0">
<segment>
<wire x1="7.62" y1="27.94" x2="-22.86" y2="27.94" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="22"/>
<label x="-22.86" y="27.94" size="1.778" layer="95"/>
</segment>
<segment>
<wire x1="-60.96" y1="58.42" x2="-30.48" y2="58.42" width="0.1524" layer="91"/>
<label x="-33.02" y="58.42" size="1.778" layer="95" rot="MR0"/>
<pinref part="X1" gate="-16" pin="F"/>
</segment>
</net>
<net name="68" class="0">
<segment>
<wire x1="7.62" y1="25.4" x2="-22.86" y2="25.4" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="23"/>
<label x="-22.86" y="25.4" size="1.778" layer="95"/>
</segment>
<segment>
<wire x1="-60.96" y1="55.88" x2="-30.48" y2="55.88" width="0.1524" layer="91"/>
<label x="-33.02" y="55.88" size="1.778" layer="95" rot="MR0"/>
<pinref part="X1" gate="-15" pin="F"/>
</segment>
</net>
<net name="69" class="0">
<segment>
<wire x1="7.62" y1="22.86" x2="-22.86" y2="22.86" width="0.1524" layer="91"/>
<pinref part="JP1" gate="A" pin="24"/>
<label x="-22.86" y="22.86" size="1.778" layer="95"/>
</segment>
<segment>
<wire x1="-60.96" y1="53.34" x2="-30.48" y2="53.34" width="0.1524" layer="91"/>
<label x="-33.02" y="53.34" size="1.778" layer="95" rot="MR0"/>
<pinref part="X1" gate="-14" pin="F"/>
</segment>
</net>
<net name="63" class="0">
<segment>
<wire x1="60.96" y1="81.28" x2="30.48" y2="81.28" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="24"/>
<label x="55.88" y="81.28" size="1.778" layer="95"/>
</segment>
</net>
<net name="86" class="0">
<segment>
<wire x1="60.96" y1="78.74" x2="30.48" y2="78.74" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="23"/>
<label x="55.88" y="78.74" size="1.778" layer="95"/>
</segment>
</net>
<net name="85" class="0">
<segment>
<wire x1="60.96" y1="76.2" x2="30.48" y2="76.2" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="22"/>
<label x="55.88" y="76.2" size="1.778" layer="95"/>
</segment>
</net>
<net name="84" class="0">
<segment>
<wire x1="60.96" y1="73.66" x2="30.48" y2="73.66" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="21"/>
<label x="55.88" y="73.66" size="1.778" layer="95"/>
</segment>
</net>
<net name="83" class="0">
<segment>
<wire x1="60.96" y1="71.12" x2="30.48" y2="71.12" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="20"/>
<label x="55.88" y="71.12" size="1.778" layer="95"/>
</segment>
</net>
<net name="82" class="0">
<segment>
<wire x1="60.96" y1="68.58" x2="30.48" y2="68.58" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="19"/>
<label x="55.88" y="68.58" size="1.778" layer="95"/>
</segment>
</net>
<net name="81" class="0">
<segment>
<wire x1="60.96" y1="66.04" x2="30.48" y2="66.04" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="18"/>
<label x="55.88" y="66.04" size="1.778" layer="95"/>
</segment>
</net>
<net name="80" class="0">
<segment>
<wire x1="60.96" y1="63.5" x2="30.48" y2="63.5" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="17"/>
<label x="55.88" y="63.5" size="1.778" layer="95"/>
</segment>
</net>
<net name="79" class="0">
<segment>
<wire x1="60.96" y1="60.96" x2="30.48" y2="60.96" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="16"/>
<label x="55.88" y="60.96" size="1.778" layer="95"/>
</segment>
</net>
<net name="77" class="0">
<segment>
<wire x1="60.96" y1="58.42" x2="30.48" y2="58.42" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="15"/>
<label x="55.88" y="58.42" size="1.778" layer="95"/>
</segment>
</net>
<net name="76" class="0">
<segment>
<wire x1="60.96" y1="55.88" x2="30.48" y2="55.88" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="14"/>
<label x="55.88" y="55.88" size="1.778" layer="95"/>
</segment>
</net>
<net name="75" class="0">
<segment>
<wire x1="96.52" y1="53.34" x2="30.48" y2="53.34" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="13"/>
<label x="55.88" y="53.34" size="1.778" layer="95"/>
<pinref part="SPI2" gate="A" pin="2"/>
</segment>
</net>
<net name="74" class="0">
<segment>
<wire x1="96.52" y1="50.8" x2="30.48" y2="50.8" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="12"/>
<label x="55.88" y="50.8" size="1.778" layer="95"/>
<pinref part="SPI2" gate="A" pin="3"/>
</segment>
</net>
<net name="73" class="0">
<segment>
<wire x1="96.52" y1="48.26" x2="30.48" y2="48.26" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="11"/>
<label x="55.88" y="48.26" size="1.778" layer="95"/>
<pinref part="SPI2" gate="A" pin="4"/>
</segment>
</net>
<net name="72" class="0">
<segment>
<wire x1="96.52" y1="45.72" x2="30.48" y2="45.72" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="10"/>
<label x="55.88" y="45.72" size="1.778" layer="95"/>
<pinref part="SPI2" gate="A" pin="5"/>
</segment>
</net>
<net name="71" class="0">
<segment>
<wire x1="60.96" y1="43.18" x2="30.48" y2="43.18" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="9"/>
<label x="55.88" y="43.18" size="1.778" layer="95"/>
</segment>
</net>
<net name="70" class="0">
<segment>
<wire x1="60.96" y1="40.64" x2="30.48" y2="40.64" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="8"/>
<label x="55.88" y="40.64" size="1.778" layer="95"/>
</segment>
</net>
<net name="5V" class="0">
<segment>
<wire x1="73.66" y1="38.1" x2="30.48" y2="38.1" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="7"/>
<label x="55.88" y="38.1" size="1.778" layer="95"/>
<pinref part="SPI1" gate="A" pin="1"/>
</segment>
<segment>
<pinref part="JP3" gate="G$1" pin="1"/>
<wire x1="-7.62" y1="96.52" x2="-30.48" y2="96.52" width="0.1524" layer="91"/>
<label x="-30.48" y="96.52" size="1.778" layer="95"/>
</segment>
</net>
<net name="48" class="0">
<segment>
<wire x1="73.66" y1="35.56" x2="30.48" y2="35.56" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="6"/>
<label x="55.88" y="35.56" size="1.778" layer="95"/>
<pinref part="SPI1" gate="A" pin="2"/>
</segment>
</net>
<net name="49" class="0">
<segment>
<wire x1="73.66" y1="33.02" x2="30.48" y2="33.02" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="5"/>
<label x="55.88" y="33.02" size="1.778" layer="95"/>
<pinref part="SPI1" gate="A" pin="3"/>
</segment>
</net>
<net name="31" class="0">
<segment>
<wire x1="73.66" y1="30.48" x2="30.48" y2="30.48" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="4"/>
<label x="55.88" y="30.48" size="1.778" layer="95"/>
<pinref part="SPI1" gate="A" pin="4"/>
</segment>
</net>
<net name="32" class="0">
<segment>
<wire x1="73.66" y1="27.94" x2="30.48" y2="27.94" width="0.1524" layer="91"/>
<pinref part="JP2" gate="A" pin="3"/>
<label x="55.88" y="27.94" size="1.778" layer="95"/>
<pinref part="SPI1" gate="A" pin="5"/>
</segment>
</net>
<net name="GND" class="0">
<segment>
<pinref part="JP2" gate="A" pin="2"/>
<label x="55.88" y="25.4" size="1.778" layer="95"/>
<wire x1="73.66" y1="25.4" x2="30.48" y2="25.4" width="0.1524" layer="91"/>
<pinref part="SPI1" gate="A" pin="6"/>
<wire x1="73.66" y1="25.4" x2="93.98" y2="25.4" width="0.1524" layer="91"/>
<pinref part="SPI2" gate="A" pin="6"/>
<wire x1="93.98" y1="25.4" x2="93.98" y2="43.18" width="0.1524" layer="91"/>
<wire x1="93.98" y1="43.18" x2="96.52" y2="43.18" width="0.1524" layer="91"/>
</segment>
<segment>
<pinref part="X1" gate="-25" pin="F"/>
<wire x1="-60.96" y1="81.28" x2="-38.1" y2="81.28" width="0.1524" layer="91"/>
<label x="-43.18" y="81.28" size="1.778" layer="95"/>
<pinref part="X1" gate="-18" pin="F"/>
<pinref part="X1" gate="-19" pin="F"/>
<wire x1="-60.96" y1="63.5" x2="-60.96" y2="66.04" width="0.1524" layer="91"/>
<pinref part="X1" gate="-20" pin="F"/>
<wire x1="-60.96" y1="66.04" x2="-60.96" y2="68.58" width="0.1524" layer="91"/>
<pinref part="X1" gate="-21" pin="F"/>
<wire x1="-60.96" y1="68.58" x2="-60.96" y2="71.12" width="0.1524" layer="91"/>
<pinref part="X1" gate="-22" pin="F"/>
<wire x1="-60.96" y1="71.12" x2="-60.96" y2="73.66" width="0.1524" layer="91"/>
<pinref part="X1" gate="-23" pin="F"/>
<wire x1="-60.96" y1="73.66" x2="-60.96" y2="76.2" width="0.1524" layer="91"/>
<pinref part="X1" gate="-24" pin="F"/>
<wire x1="-60.96" y1="76.2" x2="-60.96" y2="78.74" width="0.1524" layer="91"/>
<wire x1="-60.96" y1="78.74" x2="-60.96" y2="81.28" width="0.1524" layer="91"/>
</segment>
<segment>
<pinref part="JP3" gate="G$1" pin="2"/>
<wire x1="-30.48" y1="93.98" x2="-7.62" y2="93.98" width="0.1524" layer="91"/>
<label x="-30.48" y="93.98" size="1.778" layer="95"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
<compatibility>
<note version="8.2" severity="warning">
Since Version 8.2, EAGLE supports online libraries. The ids
of those online libraries will not be understood (or retained)
with this version.
</note>
<note version="8.3" severity="warning">
Since Version 8.3, EAGLE supports URNs for individual library
assets (packages, symbols, and devices). The URNs of those assets
will not be understood (or retained) with this version.
</note>
<note version="8.3" severity="warning">
Since Version 8.3, EAGLE supports the association of 3D packages
with devices in libraries, schematics, and board files. Those 3D
packages will not be understood (or retained) with this version.
</note>
</compatibility>
</eagle>
