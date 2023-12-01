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
<package name="2X17" urn="urn:adsk.eagle:footprint:22393/1" library_version="3">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<wire x1="-21.59" y1="-1.905" x2="-20.955" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-20.955" y1="-2.54" x2="-19.685" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-19.685" y1="-2.54" x2="-19.05" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-19.05" y1="-1.905" x2="-18.415" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-18.415" y1="-2.54" x2="-17.145" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-17.145" y1="-2.54" x2="-16.51" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-16.51" y1="-1.905" x2="-15.875" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-15.875" y1="-2.54" x2="-14.605" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-14.605" y1="-2.54" x2="-13.97" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-13.97" y1="-1.905" x2="-13.335" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-13.335" y1="-2.54" x2="-12.065" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-12.065" y1="-2.54" x2="-11.43" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-11.43" y1="-1.905" x2="-10.795" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-10.795" y1="-2.54" x2="-9.525" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-9.525" y1="-2.54" x2="-8.89" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-8.89" y1="-1.905" x2="-8.255" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-8.255" y1="-2.54" x2="-6.985" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-6.985" y1="-2.54" x2="-6.35" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-21.59" y1="-1.905" x2="-21.59" y2="1.905" width="0.1524" layer="21"/>
<wire x1="-21.59" y1="1.905" x2="-20.955" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-20.955" y1="2.54" x2="-19.685" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-19.685" y1="2.54" x2="-19.05" y2="1.905" width="0.1524" layer="21"/>
<wire x1="-19.05" y1="1.905" x2="-18.415" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-18.415" y1="2.54" x2="-17.145" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-17.145" y1="2.54" x2="-16.51" y2="1.905" width="0.1524" layer="21"/>
<wire x1="-16.51" y1="1.905" x2="-15.875" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-15.875" y1="2.54" x2="-14.605" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-14.605" y1="2.54" x2="-13.97" y2="1.905" width="0.1524" layer="21"/>
<wire x1="-13.97" y1="1.905" x2="-13.335" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-13.335" y1="2.54" x2="-12.065" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-12.065" y1="2.54" x2="-11.43" y2="1.905" width="0.1524" layer="21"/>
<wire x1="-11.43" y1="1.905" x2="-10.795" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-10.795" y1="2.54" x2="-9.525" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-9.525" y1="2.54" x2="-8.89" y2="1.905" width="0.1524" layer="21"/>
<wire x1="-8.89" y1="1.905" x2="-8.255" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-8.255" y1="2.54" x2="-6.985" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-6.985" y1="2.54" x2="-6.35" y2="1.905" width="0.1524" layer="21"/>
<wire x1="-6.35" y1="1.905" x2="-5.715" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-5.715" y1="2.54" x2="-4.445" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-4.445" y1="2.54" x2="-3.81" y2="1.905" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="1.905" x2="-3.175" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-3.175" y1="2.54" x2="-1.905" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-1.905" y1="2.54" x2="-1.27" y2="1.905" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="1.905" x2="-0.635" y2="2.54" width="0.1524" layer="21"/>
<wire x1="-0.635" y1="2.54" x2="0.635" y2="2.54" width="0.1524" layer="21"/>
<wire x1="0.635" y1="2.54" x2="1.27" y2="1.905" width="0.1524" layer="21"/>
<wire x1="1.27" y1="1.905" x2="1.905" y2="2.54" width="0.1524" layer="21"/>
<wire x1="1.905" y1="2.54" x2="3.175" y2="2.54" width="0.1524" layer="21"/>
<wire x1="3.175" y1="2.54" x2="3.81" y2="1.905" width="0.1524" layer="21"/>
<wire x1="3.81" y1="1.905" x2="4.445" y2="2.54" width="0.1524" layer="21"/>
<wire x1="4.445" y1="2.54" x2="5.715" y2="2.54" width="0.1524" layer="21"/>
<wire x1="5.715" y1="2.54" x2="6.35" y2="1.905" width="0.1524" layer="21"/>
<wire x1="6.35" y1="1.905" x2="6.985" y2="2.54" width="0.1524" layer="21"/>
<wire x1="6.985" y1="2.54" x2="8.255" y2="2.54" width="0.1524" layer="21"/>
<wire x1="8.89" y1="1.905" x2="8.255" y2="2.54" width="0.1524" layer="21"/>
<wire x1="8.89" y1="1.905" x2="9.525" y2="2.54" width="0.1524" layer="21"/>
<wire x1="10.795" y1="2.54" x2="9.525" y2="2.54" width="0.1524" layer="21"/>
<wire x1="10.795" y1="2.54" x2="11.43" y2="1.905" width="0.1524" layer="21"/>
<wire x1="11.43" y1="1.905" x2="12.065" y2="2.54" width="0.1524" layer="21"/>
<wire x1="13.335" y1="2.54" x2="12.065" y2="2.54" width="0.1524" layer="21"/>
<wire x1="13.335" y1="2.54" x2="13.97" y2="1.905" width="0.1524" layer="21"/>
<wire x1="13.97" y1="1.905" x2="14.605" y2="2.54" width="0.1524" layer="21"/>
<wire x1="15.875" y1="2.54" x2="14.605" y2="2.54" width="0.1524" layer="21"/>
<wire x1="15.875" y1="2.54" x2="16.51" y2="1.905" width="0.1524" layer="21"/>
<wire x1="16.51" y1="1.905" x2="17.145" y2="2.54" width="0.1524" layer="21"/>
<wire x1="18.415" y1="2.54" x2="17.145" y2="2.54" width="0.1524" layer="21"/>
<wire x1="18.415" y1="2.54" x2="19.05" y2="1.905" width="0.1524" layer="21"/>
<wire x1="19.05" y1="1.905" x2="19.685" y2="2.54" width="0.1524" layer="21"/>
<wire x1="20.955" y1="2.54" x2="19.685" y2="2.54" width="0.1524" layer="21"/>
<wire x1="20.955" y1="2.54" x2="21.59" y2="1.905" width="0.1524" layer="21"/>
<wire x1="21.59" y1="-1.905" x2="20.955" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="20.955" y1="-2.54" x2="19.685" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="19.05" y1="-1.905" x2="19.685" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="19.05" y1="-1.905" x2="18.415" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="17.145" y1="-2.54" x2="18.415" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="17.145" y1="-2.54" x2="16.51" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="16.51" y1="-1.905" x2="15.875" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="14.605" y1="-2.54" x2="15.875" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="14.605" y1="-2.54" x2="13.97" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="13.97" y1="-1.905" x2="13.335" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="13.335" y1="-2.54" x2="12.065" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="11.43" y1="-1.905" x2="12.065" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="11.43" y1="-1.905" x2="10.795" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="10.795" y1="-2.54" x2="9.525" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="8.89" y1="-1.905" x2="9.525" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="8.89" y1="-1.905" x2="8.255" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="8.255" y1="-2.54" x2="6.985" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="6.35" y1="-1.905" x2="6.985" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="6.35" y1="-1.905" x2="5.715" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="5.715" y1="-2.54" x2="4.445" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="3.81" y1="-1.905" x2="4.445" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="3.81" y1="-1.905" x2="3.175" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="3.175" y1="-2.54" x2="1.905" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="1.27" y1="-1.905" x2="1.905" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="1.27" y1="-1.905" x2="0.635" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="0.635" y1="-2.54" x2="-0.635" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="-1.905" x2="-0.635" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="-1.905" x2="-1.905" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-1.905" y1="-2.54" x2="-3.175" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="-1.905" x2="-3.175" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="-1.905" x2="-4.445" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-4.445" y1="-2.54" x2="-5.715" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-6.35" y1="-1.905" x2="-5.715" y2="-2.54" width="0.1524" layer="21"/>
<wire x1="-19.05" y1="1.905" x2="-19.05" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-16.51" y1="1.905" x2="-16.51" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-13.97" y1="1.905" x2="-13.97" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-11.43" y1="1.905" x2="-11.43" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-8.89" y1="1.905" x2="-8.89" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-6.35" y1="1.905" x2="-6.35" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="1.905" x2="-3.81" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="1.905" x2="-1.27" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="1.27" y1="1.905" x2="1.27" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="3.81" y1="1.905" x2="3.81" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="6.35" y1="1.905" x2="6.35" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="8.89" y1="1.905" x2="8.89" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="11.43" y1="1.905" x2="11.43" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="13.97" y1="1.905" x2="13.97" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="16.51" y1="1.905" x2="16.51" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="19.05" y1="1.905" x2="19.05" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="21.59" y1="1.905" x2="21.59" y2="-1.905" width="0.1524" layer="21"/>
<pad name="1" x="-20.32" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="2" x="-20.32" y="1.27" drill="1.016" shape="octagon"/>
<pad name="3" x="-17.78" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="4" x="-17.78" y="1.27" drill="1.016" shape="octagon"/>
<pad name="5" x="-15.24" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="6" x="-15.24" y="1.27" drill="1.016" shape="octagon"/>
<pad name="7" x="-12.7" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="8" x="-12.7" y="1.27" drill="1.016" shape="octagon"/>
<pad name="9" x="-10.16" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="10" x="-10.16" y="1.27" drill="1.016" shape="octagon"/>
<pad name="11" x="-7.62" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="12" x="-7.62" y="1.27" drill="1.016" shape="octagon"/>
<pad name="13" x="-5.08" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="14" x="-5.08" y="1.27" drill="1.016" shape="octagon"/>
<pad name="15" x="-2.54" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="16" x="-2.54" y="1.27" drill="1.016" shape="octagon"/>
<pad name="17" x="0" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="18" x="0" y="1.27" drill="1.016" shape="octagon"/>
<pad name="19" x="2.54" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="20" x="2.54" y="1.27" drill="1.016" shape="octagon"/>
<pad name="21" x="5.08" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="22" x="5.08" y="1.27" drill="1.016" shape="octagon"/>
<pad name="23" x="7.62" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="24" x="7.62" y="1.27" drill="1.016" shape="octagon"/>
<pad name="25" x="10.16" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="26" x="10.16" y="1.27" drill="1.016" shape="octagon"/>
<pad name="27" x="12.7" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="28" x="12.7" y="1.27" drill="1.016" shape="octagon"/>
<pad name="29" x="15.24" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="30" x="15.24" y="1.27" drill="1.016" shape="octagon"/>
<pad name="31" x="17.78" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="32" x="17.78" y="1.27" drill="1.016" shape="octagon"/>
<pad name="33" x="20.32" y="-1.27" drill="1.016" shape="octagon"/>
<pad name="34" x="20.32" y="1.27" drill="1.016" shape="octagon"/>
<text x="-21.59" y="3.175" size="1.27" layer="25" ratio="10">&gt;NAME</text>
<text x="-21.59" y="-4.445" size="1.27" layer="27">&gt;VALUE</text>
<rectangle x1="-20.574" y1="-1.524" x2="-20.066" y2="-1.016" layer="51"/>
<rectangle x1="-20.574" y1="1.016" x2="-20.066" y2="1.524" layer="51"/>
<rectangle x1="-18.034" y1="1.016" x2="-17.526" y2="1.524" layer="51"/>
<rectangle x1="-18.034" y1="-1.524" x2="-17.526" y2="-1.016" layer="51"/>
<rectangle x1="-15.494" y1="1.016" x2="-14.986" y2="1.524" layer="51"/>
<rectangle x1="-15.494" y1="-1.524" x2="-14.986" y2="-1.016" layer="51"/>
<rectangle x1="-12.954" y1="1.016" x2="-12.446" y2="1.524" layer="51"/>
<rectangle x1="-10.414" y1="1.016" x2="-9.906" y2="1.524" layer="51"/>
<rectangle x1="-7.874" y1="1.016" x2="-7.366" y2="1.524" layer="51"/>
<rectangle x1="-12.954" y1="-1.524" x2="-12.446" y2="-1.016" layer="51"/>
<rectangle x1="-10.414" y1="-1.524" x2="-9.906" y2="-1.016" layer="51"/>
<rectangle x1="-7.874" y1="-1.524" x2="-7.366" y2="-1.016" layer="51"/>
<rectangle x1="-5.334" y1="1.016" x2="-4.826" y2="1.524" layer="51"/>
<rectangle x1="-5.334" y1="-1.524" x2="-4.826" y2="-1.016" layer="51"/>
<rectangle x1="-2.794" y1="1.016" x2="-2.286" y2="1.524" layer="51"/>
<rectangle x1="-2.794" y1="-1.524" x2="-2.286" y2="-1.016" layer="51"/>
<rectangle x1="-0.254" y1="1.016" x2="0.254" y2="1.524" layer="51"/>
<rectangle x1="-0.254" y1="-1.524" x2="0.254" y2="-1.016" layer="51"/>
<rectangle x1="2.286" y1="1.016" x2="2.794" y2="1.524" layer="51"/>
<rectangle x1="2.286" y1="-1.524" x2="2.794" y2="-1.016" layer="51"/>
<rectangle x1="4.826" y1="1.016" x2="5.334" y2="1.524" layer="51"/>
<rectangle x1="4.826" y1="-1.524" x2="5.334" y2="-1.016" layer="51"/>
<rectangle x1="7.366" y1="1.016" x2="7.874" y2="1.524" layer="51"/>
<rectangle x1="7.366" y1="-1.524" x2="7.874" y2="-1.016" layer="51"/>
<rectangle x1="9.906" y1="1.016" x2="10.414" y2="1.524" layer="51"/>
<rectangle x1="9.906" y1="-1.524" x2="10.414" y2="-1.016" layer="51"/>
<rectangle x1="12.446" y1="1.016" x2="12.954" y2="1.524" layer="51"/>
<rectangle x1="12.446" y1="-1.524" x2="12.954" y2="-1.016" layer="51"/>
<rectangle x1="14.986" y1="1.016" x2="15.494" y2="1.524" layer="51"/>
<rectangle x1="14.986" y1="-1.524" x2="15.494" y2="-1.016" layer="51"/>
<rectangle x1="17.526" y1="1.016" x2="18.034" y2="1.524" layer="51"/>
<rectangle x1="17.526" y1="-1.524" x2="18.034" y2="-1.016" layer="51"/>
<rectangle x1="20.066" y1="1.016" x2="20.574" y2="1.524" layer="51"/>
<rectangle x1="20.066" y1="-1.524" x2="20.574" y2="-1.016" layer="51"/>
</package>
<package name="2X17/90" urn="urn:adsk.eagle:footprint:22394/1" library_version="3">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<wire x1="-21.59" y1="-1.905" x2="-19.05" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-19.05" y1="-1.905" x2="-19.05" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-19.05" y1="0.635" x2="-21.59" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-21.59" y1="0.635" x2="-21.59" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-20.32" y1="6.985" x2="-20.32" y2="1.27" width="0.762" layer="21"/>
<wire x1="-19.05" y1="-1.905" x2="-16.51" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-16.51" y1="-1.905" x2="-16.51" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-16.51" y1="0.635" x2="-19.05" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-17.78" y1="6.985" x2="-17.78" y2="1.27" width="0.762" layer="21"/>
<wire x1="-16.51" y1="-1.905" x2="-13.97" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-13.97" y1="-1.905" x2="-13.97" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-13.97" y1="0.635" x2="-16.51" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-15.24" y1="6.985" x2="-15.24" y2="1.27" width="0.762" layer="21"/>
<wire x1="-13.97" y1="-1.905" x2="-11.43" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-11.43" y1="-1.905" x2="-11.43" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-11.43" y1="0.635" x2="-13.97" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-12.7" y1="6.985" x2="-12.7" y2="1.27" width="0.762" layer="21"/>
<wire x1="-11.43" y1="-1.905" x2="-8.89" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-8.89" y1="-1.905" x2="-8.89" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-8.89" y1="0.635" x2="-11.43" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-10.16" y1="6.985" x2="-10.16" y2="1.27" width="0.762" layer="21"/>
<wire x1="-8.89" y1="-1.905" x2="-6.35" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-6.35" y1="-1.905" x2="-6.35" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-6.35" y1="0.635" x2="-8.89" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-7.62" y1="6.985" x2="-7.62" y2="1.27" width="0.762" layer="21"/>
<wire x1="-6.35" y1="-1.905" x2="-3.81" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="-1.905" x2="-3.81" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="0.635" x2="-6.35" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-5.08" y1="6.985" x2="-5.08" y2="1.27" width="0.762" layer="21"/>
<wire x1="-3.81" y1="-1.905" x2="-1.27" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="-1.905" x2="-1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="0.635" x2="-3.81" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="6.985" x2="-2.54" y2="1.27" width="0.762" layer="21"/>
<wire x1="-1.27" y1="-1.905" x2="1.27" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="1.27" y1="-1.905" x2="1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="1.27" y1="0.635" x2="-1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="0" y1="6.985" x2="0" y2="1.27" width="0.762" layer="21"/>
<wire x1="1.27" y1="-1.905" x2="3.81" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="3.81" y1="-1.905" x2="3.81" y2="0.635" width="0.1524" layer="21"/>
<wire x1="3.81" y1="0.635" x2="1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="2.54" y1="6.985" x2="2.54" y2="1.27" width="0.762" layer="21"/>
<wire x1="3.81" y1="-1.905" x2="6.35" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="6.35" y1="-1.905" x2="6.35" y2="0.635" width="0.1524" layer="21"/>
<wire x1="6.35" y1="0.635" x2="3.81" y2="0.635" width="0.1524" layer="21"/>
<wire x1="5.08" y1="6.985" x2="5.08" y2="1.27" width="0.762" layer="21"/>
<wire x1="6.35" y1="-1.905" x2="8.89" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="8.89" y1="-1.905" x2="8.89" y2="0.635" width="0.1524" layer="21"/>
<wire x1="8.89" y1="0.635" x2="6.35" y2="0.635" width="0.1524" layer="21"/>
<wire x1="7.62" y1="6.985" x2="7.62" y2="1.27" width="0.762" layer="21"/>
<wire x1="8.89" y1="-1.905" x2="11.43" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="11.43" y1="-1.905" x2="11.43" y2="0.635" width="0.1524" layer="21"/>
<wire x1="11.43" y1="0.635" x2="8.89" y2="0.635" width="0.1524" layer="21"/>
<wire x1="10.16" y1="6.985" x2="10.16" y2="1.27" width="0.762" layer="21"/>
<wire x1="11.43" y1="-1.905" x2="13.97" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="13.97" y1="-1.905" x2="13.97" y2="0.635" width="0.1524" layer="21"/>
<wire x1="13.97" y1="0.635" x2="11.43" y2="0.635" width="0.1524" layer="21"/>
<wire x1="12.7" y1="6.985" x2="12.7" y2="1.27" width="0.762" layer="21"/>
<wire x1="13.97" y1="-1.905" x2="16.51" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="16.51" y1="-1.905" x2="16.51" y2="0.635" width="0.1524" layer="21"/>
<wire x1="16.51" y1="0.635" x2="13.97" y2="0.635" width="0.1524" layer="21"/>
<wire x1="15.24" y1="6.985" x2="15.24" y2="1.27" width="0.762" layer="21"/>
<wire x1="16.51" y1="-1.905" x2="19.05" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="19.05" y1="-1.905" x2="19.05" y2="0.635" width="0.1524" layer="21"/>
<wire x1="19.05" y1="0.635" x2="16.51" y2="0.635" width="0.1524" layer="21"/>
<wire x1="17.78" y1="6.985" x2="17.78" y2="1.27" width="0.762" layer="21"/>
<wire x1="19.05" y1="-1.905" x2="21.59" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="21.59" y1="-1.905" x2="21.59" y2="0.635" width="0.1524" layer="21"/>
<wire x1="21.59" y1="0.635" x2="19.05" y2="0.635" width="0.1524" layer="21"/>
<wire x1="20.32" y1="6.985" x2="20.32" y2="1.27" width="0.762" layer="21"/>
<pad name="2" x="-20.32" y="-3.81" drill="1.016" shape="octagon"/>
<pad name="4" x="-17.78" y="-3.81" drill="1.016" shape="octagon"/>
<pad name="6" x="-15.24" y="-3.81" drill="1.016" shape="octagon"/>
<pad name="8" x="-12.7" y="-3.81" drill="1.016" shape="octagon"/>
<pad name="10" x="-10.16" y="-3.81" drill="1.016" shape="octagon"/>
<pad name="12" x="-7.62" y="-3.81" drill="1.016" shape="octagon"/>
<pad name="14" x="-5.08" y="-3.81" drill="1.016" shape="octagon"/>
<pad name="16" x="-2.54" y="-3.81" drill="1.016" shape="octagon"/>
<pad name="18" x="0" y="-3.81" drill="1.016" shape="octagon"/>
<pad name="20" x="2.54" y="-3.81" drill="1.016" shape="octagon"/>
<pad name="22" x="5.08" y="-3.81" drill="1.016" shape="octagon"/>
<pad name="24" x="7.62" y="-3.81" drill="1.016" shape="octagon"/>
<pad name="26" x="10.16" y="-3.81" drill="1.016" shape="octagon"/>
<pad name="28" x="12.7" y="-3.81" drill="1.016" shape="octagon"/>
<pad name="30" x="15.24" y="-3.81" drill="1.016" shape="octagon"/>
<pad name="32" x="17.78" y="-3.81" drill="1.016" shape="octagon"/>
<pad name="34" x="20.32" y="-3.81" drill="1.016" shape="octagon"/>
<pad name="1" x="-20.32" y="-6.35" drill="1.016" shape="octagon"/>
<pad name="3" x="-17.78" y="-6.35" drill="1.016" shape="octagon"/>
<pad name="5" x="-15.24" y="-6.35" drill="1.016" shape="octagon"/>
<pad name="7" x="-12.7" y="-6.35" drill="1.016" shape="octagon"/>
<pad name="9" x="-10.16" y="-6.35" drill="1.016" shape="octagon"/>
<pad name="11" x="-7.62" y="-6.35" drill="1.016" shape="octagon"/>
<pad name="13" x="-5.08" y="-6.35" drill="1.016" shape="octagon"/>
<pad name="15" x="-2.54" y="-6.35" drill="1.016" shape="octagon"/>
<pad name="17" x="0" y="-6.35" drill="1.016" shape="octagon"/>
<pad name="19" x="2.54" y="-6.35" drill="1.016" shape="octagon"/>
<pad name="21" x="5.08" y="-6.35" drill="1.016" shape="octagon"/>
<pad name="23" x="7.62" y="-6.35" drill="1.016" shape="octagon"/>
<pad name="25" x="10.16" y="-6.35" drill="1.016" shape="octagon"/>
<pad name="27" x="12.7" y="-6.35" drill="1.016" shape="octagon"/>
<pad name="29" x="15.24" y="-6.35" drill="1.016" shape="octagon"/>
<pad name="31" x="17.78" y="-6.35" drill="1.016" shape="octagon"/>
<pad name="33" x="20.32" y="-6.35" drill="1.016" shape="octagon"/>
<text x="-22.225" y="-3.81" size="1.27" layer="25" ratio="10" rot="R90">&gt;NAME</text>
<text x="23.495" y="-3.81" size="1.27" layer="27" rot="R90">&gt;VALUE</text>
<rectangle x1="-20.701" y1="0.635" x2="-19.939" y2="1.143" layer="21"/>
<rectangle x1="-18.161" y1="0.635" x2="-17.399" y2="1.143" layer="21"/>
<rectangle x1="-15.621" y1="0.635" x2="-14.859" y2="1.143" layer="21"/>
<rectangle x1="-13.081" y1="0.635" x2="-12.319" y2="1.143" layer="21"/>
<rectangle x1="-10.541" y1="0.635" x2="-9.779" y2="1.143" layer="21"/>
<rectangle x1="-8.001" y1="0.635" x2="-7.239" y2="1.143" layer="21"/>
<rectangle x1="-5.461" y1="0.635" x2="-4.699" y2="1.143" layer="21"/>
<rectangle x1="-2.921" y1="0.635" x2="-2.159" y2="1.143" layer="21"/>
<rectangle x1="-0.381" y1="0.635" x2="0.381" y2="1.143" layer="21"/>
<rectangle x1="2.159" y1="0.635" x2="2.921" y2="1.143" layer="21"/>
<rectangle x1="4.699" y1="0.635" x2="5.461" y2="1.143" layer="21"/>
<rectangle x1="7.239" y1="0.635" x2="8.001" y2="1.143" layer="21"/>
<rectangle x1="9.779" y1="0.635" x2="10.541" y2="1.143" layer="21"/>
<rectangle x1="12.319" y1="0.635" x2="13.081" y2="1.143" layer="21"/>
<rectangle x1="14.859" y1="0.635" x2="15.621" y2="1.143" layer="21"/>
<rectangle x1="17.399" y1="0.635" x2="18.161" y2="1.143" layer="21"/>
<rectangle x1="19.939" y1="0.635" x2="20.701" y2="1.143" layer="21"/>
<rectangle x1="-20.701" y1="-2.921" x2="-19.939" y2="-1.905" layer="21"/>
<rectangle x1="-18.161" y1="-2.921" x2="-17.399" y2="-1.905" layer="21"/>
<rectangle x1="-20.701" y1="-5.461" x2="-19.939" y2="-4.699" layer="21"/>
<rectangle x1="-20.701" y1="-4.699" x2="-19.939" y2="-2.921" layer="51"/>
<rectangle x1="-18.161" y1="-4.699" x2="-17.399" y2="-2.921" layer="51"/>
<rectangle x1="-18.161" y1="-5.461" x2="-17.399" y2="-4.699" layer="21"/>
<rectangle x1="-15.621" y1="-2.921" x2="-14.859" y2="-1.905" layer="21"/>
<rectangle x1="-13.081" y1="-2.921" x2="-12.319" y2="-1.905" layer="21"/>
<rectangle x1="-15.621" y1="-5.461" x2="-14.859" y2="-4.699" layer="21"/>
<rectangle x1="-15.621" y1="-4.699" x2="-14.859" y2="-2.921" layer="51"/>
<rectangle x1="-13.081" y1="-4.699" x2="-12.319" y2="-2.921" layer="51"/>
<rectangle x1="-13.081" y1="-5.461" x2="-12.319" y2="-4.699" layer="21"/>
<rectangle x1="-10.541" y1="-2.921" x2="-9.779" y2="-1.905" layer="21"/>
<rectangle x1="-10.541" y1="-5.461" x2="-9.779" y2="-4.699" layer="21"/>
<rectangle x1="-10.541" y1="-4.699" x2="-9.779" y2="-2.921" layer="51"/>
<rectangle x1="-8.001" y1="-2.921" x2="-7.239" y2="-1.905" layer="21"/>
<rectangle x1="-5.461" y1="-2.921" x2="-4.699" y2="-1.905" layer="21"/>
<rectangle x1="-8.001" y1="-5.461" x2="-7.239" y2="-4.699" layer="21"/>
<rectangle x1="-8.001" y1="-4.699" x2="-7.239" y2="-2.921" layer="51"/>
<rectangle x1="-5.461" y1="-4.699" x2="-4.699" y2="-2.921" layer="51"/>
<rectangle x1="-5.461" y1="-5.461" x2="-4.699" y2="-4.699" layer="21"/>
<rectangle x1="-2.921" y1="-2.921" x2="-2.159" y2="-1.905" layer="21"/>
<rectangle x1="-0.381" y1="-2.921" x2="0.381" y2="-1.905" layer="21"/>
<rectangle x1="-2.921" y1="-5.461" x2="-2.159" y2="-4.699" layer="21"/>
<rectangle x1="-2.921" y1="-4.699" x2="-2.159" y2="-2.921" layer="51"/>
<rectangle x1="-0.381" y1="-4.699" x2="0.381" y2="-2.921" layer="51"/>
<rectangle x1="-0.381" y1="-5.461" x2="0.381" y2="-4.699" layer="21"/>
<rectangle x1="2.159" y1="-2.921" x2="2.921" y2="-1.905" layer="21"/>
<rectangle x1="2.159" y1="-5.461" x2="2.921" y2="-4.699" layer="21"/>
<rectangle x1="2.159" y1="-4.699" x2="2.921" y2="-2.921" layer="51"/>
<rectangle x1="4.699" y1="-2.921" x2="5.461" y2="-1.905" layer="21"/>
<rectangle x1="7.239" y1="-2.921" x2="8.001" y2="-1.905" layer="21"/>
<rectangle x1="4.699" y1="-5.461" x2="5.461" y2="-4.699" layer="21"/>
<rectangle x1="4.699" y1="-4.699" x2="5.461" y2="-2.921" layer="51"/>
<rectangle x1="7.239" y1="-4.699" x2="8.001" y2="-2.921" layer="51"/>
<rectangle x1="7.239" y1="-5.461" x2="8.001" y2="-4.699" layer="21"/>
<rectangle x1="9.779" y1="-2.921" x2="10.541" y2="-1.905" layer="21"/>
<rectangle x1="12.319" y1="-2.921" x2="13.081" y2="-1.905" layer="21"/>
<rectangle x1="9.779" y1="-5.461" x2="10.541" y2="-4.699" layer="21"/>
<rectangle x1="9.779" y1="-4.699" x2="10.541" y2="-2.921" layer="51"/>
<rectangle x1="12.319" y1="-4.699" x2="13.081" y2="-2.921" layer="51"/>
<rectangle x1="12.319" y1="-5.461" x2="13.081" y2="-4.699" layer="21"/>
<rectangle x1="14.859" y1="-2.921" x2="15.621" y2="-1.905" layer="21"/>
<rectangle x1="14.859" y1="-5.461" x2="15.621" y2="-4.699" layer="21"/>
<rectangle x1="14.859" y1="-4.699" x2="15.621" y2="-2.921" layer="51"/>
<rectangle x1="17.399" y1="-2.921" x2="18.161" y2="-1.905" layer="21"/>
<rectangle x1="19.939" y1="-2.921" x2="20.701" y2="-1.905" layer="21"/>
<rectangle x1="17.399" y1="-5.461" x2="18.161" y2="-4.699" layer="21"/>
<rectangle x1="17.399" y1="-4.699" x2="18.161" y2="-2.921" layer="51"/>
<rectangle x1="19.939" y1="-4.699" x2="20.701" y2="-2.921" layer="51"/>
<rectangle x1="19.939" y1="-5.461" x2="20.701" y2="-4.699" layer="21"/>
</package>
<package name="1X03" urn="urn:adsk.eagle:footprint:22340/1" library_version="3">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<wire x1="-3.175" y1="1.27" x2="-1.905" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-1.905" y1="1.27" x2="-1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="0.635" x2="-1.27" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="-0.635" x2="-1.905" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="0.635" x2="-0.635" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-0.635" y1="1.27" x2="0.635" y2="1.27" width="0.1524" layer="21"/>
<wire x1="0.635" y1="1.27" x2="1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="1.27" y1="0.635" x2="1.27" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="1.27" y1="-0.635" x2="0.635" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="0.635" y1="-1.27" x2="-0.635" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-0.635" y1="-1.27" x2="-1.27" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="0.635" x2="-3.81" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-3.175" y1="1.27" x2="-3.81" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="-0.635" x2="-3.175" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-1.905" y1="-1.27" x2="-3.175" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="1.27" y1="0.635" x2="1.905" y2="1.27" width="0.1524" layer="21"/>
<wire x1="1.905" y1="1.27" x2="3.175" y2="1.27" width="0.1524" layer="21"/>
<wire x1="3.175" y1="1.27" x2="3.81" y2="0.635" width="0.1524" layer="21"/>
<wire x1="3.81" y1="0.635" x2="3.81" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="3.81" y1="-0.635" x2="3.175" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="3.175" y1="-1.27" x2="1.905" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="1.905" y1="-1.27" x2="1.27" y2="-0.635" width="0.1524" layer="21"/>
<pad name="1" x="-2.54" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="2" x="0" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="3" x="2.54" y="0" drill="1.016" shape="long" rot="R90"/>
<text x="-3.8862" y="1.8288" size="1.27" layer="25" ratio="10">&gt;NAME</text>
<text x="-3.81" y="-3.175" size="1.27" layer="27">&gt;VALUE</text>
<rectangle x1="-0.254" y1="-0.254" x2="0.254" y2="0.254" layer="51"/>
<rectangle x1="-2.794" y1="-0.254" x2="-2.286" y2="0.254" layer="51"/>
<rectangle x1="2.286" y1="-0.254" x2="2.794" y2="0.254" layer="51"/>
</package>
<package name="1X03/90" urn="urn:adsk.eagle:footprint:22341/1" library_version="3">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<wire x1="-3.81" y1="-1.905" x2="-1.27" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="-1.905" x2="-1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="0.635" x2="-3.81" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="0.635" x2="-3.81" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="6.985" x2="-2.54" y2="1.27" width="0.762" layer="21"/>
<wire x1="-1.27" y1="-1.905" x2="1.27" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="1.27" y1="-1.905" x2="1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="1.27" y1="0.635" x2="-1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="0" y1="6.985" x2="0" y2="1.27" width="0.762" layer="21"/>
<wire x1="1.27" y1="-1.905" x2="3.81" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="3.81" y1="-1.905" x2="3.81" y2="0.635" width="0.1524" layer="21"/>
<wire x1="3.81" y1="0.635" x2="1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="2.54" y1="6.985" x2="2.54" y2="1.27" width="0.762" layer="21"/>
<pad name="1" x="-2.54" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="2" x="0" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="3" x="2.54" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<text x="-4.445" y="-3.81" size="1.27" layer="25" ratio="10" rot="R90">&gt;NAME</text>
<text x="5.715" y="-3.81" size="1.27" layer="27" rot="R90">&gt;VALUE</text>
<rectangle x1="-2.921" y1="0.635" x2="-2.159" y2="1.143" layer="21"/>
<rectangle x1="-0.381" y1="0.635" x2="0.381" y2="1.143" layer="21"/>
<rectangle x1="2.159" y1="0.635" x2="2.921" y2="1.143" layer="21"/>
<rectangle x1="-2.921" y1="-2.921" x2="-2.159" y2="-1.905" layer="21"/>
<rectangle x1="-0.381" y1="-2.921" x2="0.381" y2="-1.905" layer="21"/>
<rectangle x1="2.159" y1="-2.921" x2="2.921" y2="-1.905" layer="21"/>
</package>
<package name="1X11" urn="urn:adsk.eagle:footprint:22267/1" library_version="3">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<wire x1="9.525" y1="1.27" x2="10.795" y2="1.27" width="0.1524" layer="21"/>
<wire x1="10.795" y1="1.27" x2="11.43" y2="0.635" width="0.1524" layer="21"/>
<wire x1="11.43" y1="0.635" x2="11.43" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="11.43" y1="-0.635" x2="10.795" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="6.35" y1="0.635" x2="6.985" y2="1.27" width="0.1524" layer="21"/>
<wire x1="6.985" y1="1.27" x2="8.255" y2="1.27" width="0.1524" layer="21"/>
<wire x1="8.255" y1="1.27" x2="8.89" y2="0.635" width="0.1524" layer="21"/>
<wire x1="8.89" y1="0.635" x2="8.89" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="8.89" y1="-0.635" x2="8.255" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="8.255" y1="-1.27" x2="6.985" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="6.985" y1="-1.27" x2="6.35" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="9.525" y1="1.27" x2="8.89" y2="0.635" width="0.1524" layer="21"/>
<wire x1="8.89" y1="-0.635" x2="9.525" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="10.795" y1="-1.27" x2="9.525" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="1.905" y1="1.27" x2="3.175" y2="1.27" width="0.1524" layer="21"/>
<wire x1="3.175" y1="1.27" x2="3.81" y2="0.635" width="0.1524" layer="21"/>
<wire x1="3.81" y1="0.635" x2="3.81" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="3.81" y1="-0.635" x2="3.175" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="3.81" y1="0.635" x2="4.445" y2="1.27" width="0.1524" layer="21"/>
<wire x1="4.445" y1="1.27" x2="5.715" y2="1.27" width="0.1524" layer="21"/>
<wire x1="5.715" y1="1.27" x2="6.35" y2="0.635" width="0.1524" layer="21"/>
<wire x1="6.35" y1="0.635" x2="6.35" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="6.35" y1="-0.635" x2="5.715" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="5.715" y1="-1.27" x2="4.445" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="4.445" y1="-1.27" x2="3.81" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="0.635" x2="-0.635" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-0.635" y1="1.27" x2="0.635" y2="1.27" width="0.1524" layer="21"/>
<wire x1="0.635" y1="1.27" x2="1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="1.27" y1="0.635" x2="1.27" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="1.27" y1="-0.635" x2="0.635" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="0.635" y1="-1.27" x2="-0.635" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-0.635" y1="-1.27" x2="-1.27" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="1.905" y1="1.27" x2="1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="1.27" y1="-0.635" x2="1.905" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="3.175" y1="-1.27" x2="1.905" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-5.715" y1="1.27" x2="-4.445" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-4.445" y1="1.27" x2="-3.81" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="0.635" x2="-3.81" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="-0.635" x2="-4.445" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="0.635" x2="-3.175" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-3.175" y1="1.27" x2="-1.905" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-1.905" y1="1.27" x2="-1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="0.635" x2="-1.27" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="-0.635" x2="-1.905" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-1.905" y1="-1.27" x2="-3.175" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-3.175" y1="-1.27" x2="-3.81" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-8.89" y1="0.635" x2="-8.255" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-8.255" y1="1.27" x2="-6.985" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-6.985" y1="1.27" x2="-6.35" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-6.35" y1="0.635" x2="-6.35" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-6.35" y1="-0.635" x2="-6.985" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-6.985" y1="-1.27" x2="-8.255" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-8.255" y1="-1.27" x2="-8.89" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-5.715" y1="1.27" x2="-6.35" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-6.35" y1="-0.635" x2="-5.715" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-4.445" y1="-1.27" x2="-5.715" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-13.335" y1="1.27" x2="-12.065" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-12.065" y1="1.27" x2="-11.43" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-11.43" y1="0.635" x2="-11.43" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-11.43" y1="-0.635" x2="-12.065" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-11.43" y1="0.635" x2="-10.795" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-10.795" y1="1.27" x2="-9.525" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-9.525" y1="1.27" x2="-8.89" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-8.89" y1="0.635" x2="-8.89" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-8.89" y1="-0.635" x2="-9.525" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-9.525" y1="-1.27" x2="-10.795" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-10.795" y1="-1.27" x2="-11.43" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-13.97" y1="0.635" x2="-13.97" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-13.335" y1="1.27" x2="-13.97" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-13.97" y1="-0.635" x2="-13.335" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-12.065" y1="-1.27" x2="-13.335" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="12.065" y1="1.27" x2="13.335" y2="1.27" width="0.1524" layer="21"/>
<wire x1="13.335" y1="1.27" x2="13.97" y2="0.635" width="0.1524" layer="21"/>
<wire x1="13.97" y1="0.635" x2="13.97" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="13.97" y1="-0.635" x2="13.335" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="12.065" y1="1.27" x2="11.43" y2="0.635" width="0.1524" layer="21"/>
<wire x1="11.43" y1="-0.635" x2="12.065" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="13.335" y1="-1.27" x2="12.065" y2="-1.27" width="0.1524" layer="21"/>
<pad name="1" x="-12.7" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="2" x="-10.16" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="3" x="-7.62" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="4" x="-5.08" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="5" x="-2.54" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="6" x="0" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="7" x="2.54" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="8" x="5.08" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="9" x="7.62" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="10" x="10.16" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="11" x="12.7" y="0" drill="1.016" shape="long" rot="R90"/>
<text x="-14.0462" y="1.8288" size="1.27" layer="25" ratio="10">&gt;NAME</text>
<text x="-13.97" y="-3.175" size="1.27" layer="27">&gt;VALUE</text>
<rectangle x1="9.906" y1="-0.254" x2="10.414" y2="0.254" layer="51"/>
<rectangle x1="7.366" y1="-0.254" x2="7.874" y2="0.254" layer="51"/>
<rectangle x1="4.826" y1="-0.254" x2="5.334" y2="0.254" layer="51"/>
<rectangle x1="2.286" y1="-0.254" x2="2.794" y2="0.254" layer="51"/>
<rectangle x1="-0.254" y1="-0.254" x2="0.254" y2="0.254" layer="51"/>
<rectangle x1="-2.794" y1="-0.254" x2="-2.286" y2="0.254" layer="51"/>
<rectangle x1="-5.334" y1="-0.254" x2="-4.826" y2="0.254" layer="51"/>
<rectangle x1="-7.874" y1="-0.254" x2="-7.366" y2="0.254" layer="51"/>
<rectangle x1="-10.414" y1="-0.254" x2="-9.906" y2="0.254" layer="51"/>
<rectangle x1="-12.954" y1="-0.254" x2="-12.446" y2="0.254" layer="51"/>
<rectangle x1="12.446" y1="-0.254" x2="12.954" y2="0.254" layer="51"/>
</package>
<package name="1X11/90" urn="urn:adsk.eagle:footprint:22271/1" library_version="3">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<wire x1="-13.97" y1="-1.905" x2="-11.43" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-11.43" y1="-1.905" x2="-11.43" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-11.43" y1="0.635" x2="-13.97" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-13.97" y1="0.635" x2="-13.97" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-12.7" y1="6.985" x2="-12.7" y2="1.27" width="0.762" layer="21"/>
<wire x1="-11.43" y1="-1.905" x2="-8.89" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-8.89" y1="-1.905" x2="-8.89" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-8.89" y1="0.635" x2="-11.43" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-10.16" y1="6.985" x2="-10.16" y2="1.27" width="0.762" layer="21"/>
<wire x1="-8.89" y1="-1.905" x2="-6.35" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-6.35" y1="-1.905" x2="-6.35" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-6.35" y1="0.635" x2="-8.89" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-7.62" y1="6.985" x2="-7.62" y2="1.27" width="0.762" layer="21"/>
<wire x1="-6.35" y1="-1.905" x2="-3.81" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="-1.905" x2="-3.81" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="0.635" x2="-6.35" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-5.08" y1="6.985" x2="-5.08" y2="1.27" width="0.762" layer="21"/>
<wire x1="-3.81" y1="-1.905" x2="-1.27" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="-1.905" x2="-1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="0.635" x2="-3.81" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="6.985" x2="-2.54" y2="1.27" width="0.762" layer="21"/>
<wire x1="-1.27" y1="-1.905" x2="1.27" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="1.27" y1="-1.905" x2="1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="1.27" y1="0.635" x2="-1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="0" y1="6.985" x2="0" y2="1.27" width="0.762" layer="21"/>
<wire x1="1.27" y1="-1.905" x2="3.81" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="3.81" y1="-1.905" x2="3.81" y2="0.635" width="0.1524" layer="21"/>
<wire x1="3.81" y1="0.635" x2="1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="2.54" y1="6.985" x2="2.54" y2="1.27" width="0.762" layer="21"/>
<wire x1="3.81" y1="-1.905" x2="6.35" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="6.35" y1="-1.905" x2="6.35" y2="0.635" width="0.1524" layer="21"/>
<wire x1="6.35" y1="0.635" x2="3.81" y2="0.635" width="0.1524" layer="21"/>
<wire x1="5.08" y1="6.985" x2="5.08" y2="1.27" width="0.762" layer="21"/>
<wire x1="6.35" y1="-1.905" x2="8.89" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="8.89" y1="-1.905" x2="8.89" y2="0.635" width="0.1524" layer="21"/>
<wire x1="8.89" y1="0.635" x2="6.35" y2="0.635" width="0.1524" layer="21"/>
<wire x1="7.62" y1="6.985" x2="7.62" y2="1.27" width="0.762" layer="21"/>
<wire x1="8.89" y1="-1.905" x2="11.43" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="11.43" y1="-1.905" x2="11.43" y2="0.635" width="0.1524" layer="21"/>
<wire x1="11.43" y1="0.635" x2="8.89" y2="0.635" width="0.1524" layer="21"/>
<wire x1="10.16" y1="6.985" x2="10.16" y2="1.27" width="0.762" layer="21"/>
<wire x1="11.43" y1="-1.905" x2="13.97" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="13.97" y1="-1.905" x2="13.97" y2="0.635" width="0.1524" layer="21"/>
<wire x1="13.97" y1="0.635" x2="11.43" y2="0.635" width="0.1524" layer="21"/>
<wire x1="12.7" y1="6.985" x2="12.7" y2="1.27" width="0.762" layer="21"/>
<pad name="1" x="-12.7" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="2" x="-10.16" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="3" x="-7.62" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="4" x="-5.08" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="5" x="-2.54" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="6" x="0" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="7" x="2.54" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="8" x="5.08" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="9" x="7.62" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="10" x="10.16" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="11" x="12.7" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<text x="-14.605" y="-3.81" size="1.27" layer="25" ratio="10" rot="R90">&gt;NAME</text>
<text x="15.875" y="-4.445" size="1.27" layer="27" rot="R90">&gt;VALUE</text>
<rectangle x1="-13.081" y1="0.635" x2="-12.319" y2="1.143" layer="21"/>
<rectangle x1="-10.541" y1="0.635" x2="-9.779" y2="1.143" layer="21"/>
<rectangle x1="-8.001" y1="0.635" x2="-7.239" y2="1.143" layer="21"/>
<rectangle x1="-5.461" y1="0.635" x2="-4.699" y2="1.143" layer="21"/>
<rectangle x1="-2.921" y1="0.635" x2="-2.159" y2="1.143" layer="21"/>
<rectangle x1="-0.381" y1="0.635" x2="0.381" y2="1.143" layer="21"/>
<rectangle x1="2.159" y1="0.635" x2="2.921" y2="1.143" layer="21"/>
<rectangle x1="4.699" y1="0.635" x2="5.461" y2="1.143" layer="21"/>
<rectangle x1="7.239" y1="0.635" x2="8.001" y2="1.143" layer="21"/>
<rectangle x1="9.779" y1="0.635" x2="10.541" y2="1.143" layer="21"/>
<rectangle x1="12.319" y1="0.635" x2="13.081" y2="1.143" layer="21"/>
<rectangle x1="-13.081" y1="-2.921" x2="-12.319" y2="-1.905" layer="21"/>
<rectangle x1="-10.541" y1="-2.921" x2="-9.779" y2="-1.905" layer="21"/>
<rectangle x1="-8.001" y1="-2.921" x2="-7.239" y2="-1.905" layer="21"/>
<rectangle x1="-5.461" y1="-2.921" x2="-4.699" y2="-1.905" layer="21"/>
<rectangle x1="-2.921" y1="-2.921" x2="-2.159" y2="-1.905" layer="21"/>
<rectangle x1="-0.381" y1="-2.921" x2="0.381" y2="-1.905" layer="21"/>
<rectangle x1="2.159" y1="-2.921" x2="2.921" y2="-1.905" layer="21"/>
<rectangle x1="4.699" y1="-2.921" x2="5.461" y2="-1.905" layer="21"/>
<rectangle x1="7.239" y1="-2.921" x2="8.001" y2="-1.905" layer="21"/>
<rectangle x1="9.779" y1="-2.921" x2="10.541" y2="-1.905" layer="21"/>
<rectangle x1="12.319" y1="-2.921" x2="13.081" y2="-1.905" layer="21"/>
</package>
</packages>
<packages3d>
<package3d name="2X17" urn="urn:adsk.eagle:package:22495/2" type="model" library_version="3">
<description>PIN HEADER</description>
<packageinstances>
<packageinstance name="2X17"/>
</packageinstances>
</package3d>
<package3d name="2X17/90" urn="urn:adsk.eagle:package:22494/2" type="model" library_version="3">
<description>PIN HEADER</description>
<packageinstances>
<packageinstance name="2X17/90"/>
</packageinstances>
</package3d>
<package3d name="1X03" urn="urn:adsk.eagle:package:22458/2" type="model" library_version="3">
<description>PIN HEADER</description>
<packageinstances>
<packageinstance name="1X03"/>
</packageinstances>
</package3d>
<package3d name="1X03/90" urn="urn:adsk.eagle:package:22459/2" type="model" library_version="3">
<description>PIN HEADER</description>
<packageinstances>
<packageinstance name="1X03/90"/>
</packageinstances>
</package3d>
<package3d name="1X11" urn="urn:adsk.eagle:package:22410/2" type="model" library_version="3">
<description>PIN HEADER</description>
<packageinstances>
<packageinstance name="1X11"/>
</packageinstances>
</package3d>
<package3d name="1X11/90" urn="urn:adsk.eagle:package:22416/2" type="model" library_version="3">
<description>PIN HEADER</description>
<packageinstances>
<packageinstance name="1X11/90"/>
</packageinstances>
</package3d>
</packages3d>
<symbols>
<symbol name="PINH2X17" urn="urn:adsk.eagle:symbol:22392/1" library_version="3">
<wire x1="-6.35" y1="-22.86" x2="8.89" y2="-22.86" width="0.4064" layer="94"/>
<wire x1="8.89" y1="-22.86" x2="8.89" y2="22.86" width="0.4064" layer="94"/>
<wire x1="8.89" y1="22.86" x2="-6.35" y2="22.86" width="0.4064" layer="94"/>
<wire x1="-6.35" y1="22.86" x2="-6.35" y2="-22.86" width="0.4064" layer="94"/>
<text x="-6.35" y="23.495" size="1.778" layer="95">&gt;NAME</text>
<text x="-6.35" y="-25.4" size="1.778" layer="96">&gt;VALUE</text>
<pin name="1" x="-2.54" y="20.32" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="2" x="5.08" y="20.32" visible="pad" length="short" direction="pas" function="dot" rot="R180"/>
<pin name="3" x="-2.54" y="17.78" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="4" x="5.08" y="17.78" visible="pad" length="short" direction="pas" function="dot" rot="R180"/>
<pin name="5" x="-2.54" y="15.24" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="6" x="5.08" y="15.24" visible="pad" length="short" direction="pas" function="dot" rot="R180"/>
<pin name="7" x="-2.54" y="12.7" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="8" x="5.08" y="12.7" visible="pad" length="short" direction="pas" function="dot" rot="R180"/>
<pin name="9" x="-2.54" y="10.16" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="10" x="5.08" y="10.16" visible="pad" length="short" direction="pas" function="dot" rot="R180"/>
<pin name="11" x="-2.54" y="7.62" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="12" x="5.08" y="7.62" visible="pad" length="short" direction="pas" function="dot" rot="R180"/>
<pin name="13" x="-2.54" y="5.08" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="14" x="5.08" y="5.08" visible="pad" length="short" direction="pas" function="dot" rot="R180"/>
<pin name="15" x="-2.54" y="2.54" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="16" x="5.08" y="2.54" visible="pad" length="short" direction="pas" function="dot" rot="R180"/>
<pin name="17" x="-2.54" y="0" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="18" x="5.08" y="0" visible="pad" length="short" direction="pas" function="dot" rot="R180"/>
<pin name="19" x="-2.54" y="-2.54" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="20" x="5.08" y="-2.54" visible="pad" length="short" direction="pas" function="dot" rot="R180"/>
<pin name="21" x="-2.54" y="-5.08" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="22" x="5.08" y="-5.08" visible="pad" length="short" direction="pas" function="dot" rot="R180"/>
<pin name="23" x="-2.54" y="-7.62" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="24" x="5.08" y="-7.62" visible="pad" length="short" direction="pas" function="dot" rot="R180"/>
<pin name="25" x="-2.54" y="-10.16" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="26" x="5.08" y="-10.16" visible="pad" length="short" direction="pas" function="dot" rot="R180"/>
<pin name="27" x="-2.54" y="-12.7" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="28" x="5.08" y="-12.7" visible="pad" length="short" direction="pas" function="dot" rot="R180"/>
<pin name="29" x="-2.54" y="-15.24" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="30" x="5.08" y="-15.24" visible="pad" length="short" direction="pas" function="dot" rot="R180"/>
<pin name="31" x="-2.54" y="-17.78" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="32" x="5.08" y="-17.78" visible="pad" length="short" direction="pas" function="dot" rot="R180"/>
<pin name="33" x="-2.54" y="-20.32" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="34" x="5.08" y="-20.32" visible="pad" length="short" direction="pas" function="dot" rot="R180"/>
</symbol>
<symbol name="PINHD3" urn="urn:adsk.eagle:symbol:22339/1" library_version="3">
<wire x1="-6.35" y1="-5.08" x2="1.27" y2="-5.08" width="0.4064" layer="94"/>
<wire x1="1.27" y1="-5.08" x2="1.27" y2="5.08" width="0.4064" layer="94"/>
<wire x1="1.27" y1="5.08" x2="-6.35" y2="5.08" width="0.4064" layer="94"/>
<wire x1="-6.35" y1="5.08" x2="-6.35" y2="-5.08" width="0.4064" layer="94"/>
<text x="-6.35" y="5.715" size="1.778" layer="95">&gt;NAME</text>
<text x="-6.35" y="-7.62" size="1.778" layer="96">&gt;VALUE</text>
<pin name="1" x="-2.54" y="2.54" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="2" x="-2.54" y="0" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="3" x="-2.54" y="-2.54" visible="pad" length="short" direction="pas" function="dot"/>
</symbol>
<symbol name="PINHD11" urn="urn:adsk.eagle:symbol:22270/1" library_version="3">
<wire x1="-6.35" y1="-15.24" x2="1.27" y2="-15.24" width="0.4064" layer="94"/>
<wire x1="1.27" y1="-15.24" x2="1.27" y2="15.24" width="0.4064" layer="94"/>
<wire x1="1.27" y1="15.24" x2="-6.35" y2="15.24" width="0.4064" layer="94"/>
<wire x1="-6.35" y1="15.24" x2="-6.35" y2="-15.24" width="0.4064" layer="94"/>
<text x="-6.35" y="15.875" size="1.778" layer="95">&gt;NAME</text>
<text x="-6.35" y="-17.78" size="1.778" layer="96">&gt;VALUE</text>
<pin name="1" x="-2.54" y="12.7" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="2" x="-2.54" y="10.16" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="3" x="-2.54" y="7.62" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="4" x="-2.54" y="5.08" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="5" x="-2.54" y="2.54" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="6" x="-2.54" y="0" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="7" x="-2.54" y="-2.54" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="8" x="-2.54" y="-5.08" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="9" x="-2.54" y="-7.62" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="10" x="-2.54" y="-10.16" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="11" x="-2.54" y="-12.7" visible="pad" length="short" direction="pas" function="dot"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="PINHD-2X17" urn="urn:adsk.eagle:component:22547/3" prefix="JP" uservalue="yes" library_version="3">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<gates>
<gate name="G$1" symbol="PINH2X17" x="0" y="0"/>
</gates>
<devices>
<device name="" package="2X17">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="10" pad="10"/>
<connect gate="G$1" pin="11" pad="11"/>
<connect gate="G$1" pin="12" pad="12"/>
<connect gate="G$1" pin="13" pad="13"/>
<connect gate="G$1" pin="14" pad="14"/>
<connect gate="G$1" pin="15" pad="15"/>
<connect gate="G$1" pin="16" pad="16"/>
<connect gate="G$1" pin="17" pad="17"/>
<connect gate="G$1" pin="18" pad="18"/>
<connect gate="G$1" pin="19" pad="19"/>
<connect gate="G$1" pin="2" pad="2"/>
<connect gate="G$1" pin="20" pad="20"/>
<connect gate="G$1" pin="21" pad="21"/>
<connect gate="G$1" pin="22" pad="22"/>
<connect gate="G$1" pin="23" pad="23"/>
<connect gate="G$1" pin="24" pad="24"/>
<connect gate="G$1" pin="25" pad="25"/>
<connect gate="G$1" pin="26" pad="26"/>
<connect gate="G$1" pin="27" pad="27"/>
<connect gate="G$1" pin="28" pad="28"/>
<connect gate="G$1" pin="29" pad="29"/>
<connect gate="G$1" pin="3" pad="3"/>
<connect gate="G$1" pin="30" pad="30"/>
<connect gate="G$1" pin="31" pad="31"/>
<connect gate="G$1" pin="32" pad="32"/>
<connect gate="G$1" pin="33" pad="33"/>
<connect gate="G$1" pin="34" pad="34"/>
<connect gate="G$1" pin="4" pad="4"/>
<connect gate="G$1" pin="5" pad="5"/>
<connect gate="G$1" pin="6" pad="6"/>
<connect gate="G$1" pin="7" pad="7"/>
<connect gate="G$1" pin="8" pad="8"/>
<connect gate="G$1" pin="9" pad="9"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:22495/2"/>
</package3dinstances>
<technologies>
<technology name=""/>
</technologies>
</device>
<device name="/90" package="2X17/90">
<connects>
<connect gate="G$1" pin="1" pad="1"/>
<connect gate="G$1" pin="10" pad="10"/>
<connect gate="G$1" pin="11" pad="11"/>
<connect gate="G$1" pin="12" pad="12"/>
<connect gate="G$1" pin="13" pad="13"/>
<connect gate="G$1" pin="14" pad="14"/>
<connect gate="G$1" pin="15" pad="15"/>
<connect gate="G$1" pin="16" pad="16"/>
<connect gate="G$1" pin="17" pad="17"/>
<connect gate="G$1" pin="18" pad="18"/>
<connect gate="G$1" pin="19" pad="19"/>
<connect gate="G$1" pin="2" pad="2"/>
<connect gate="G$1" pin="20" pad="20"/>
<connect gate="G$1" pin="21" pad="21"/>
<connect gate="G$1" pin="22" pad="22"/>
<connect gate="G$1" pin="23" pad="23"/>
<connect gate="G$1" pin="24" pad="24"/>
<connect gate="G$1" pin="25" pad="25"/>
<connect gate="G$1" pin="26" pad="26"/>
<connect gate="G$1" pin="27" pad="27"/>
<connect gate="G$1" pin="28" pad="28"/>
<connect gate="G$1" pin="29" pad="29"/>
<connect gate="G$1" pin="3" pad="3"/>
<connect gate="G$1" pin="30" pad="30"/>
<connect gate="G$1" pin="31" pad="31"/>
<connect gate="G$1" pin="32" pad="32"/>
<connect gate="G$1" pin="33" pad="33"/>
<connect gate="G$1" pin="34" pad="34"/>
<connect gate="G$1" pin="4" pad="4"/>
<connect gate="G$1" pin="5" pad="5"/>
<connect gate="G$1" pin="6" pad="6"/>
<connect gate="G$1" pin="7" pad="7"/>
<connect gate="G$1" pin="8" pad="8"/>
<connect gate="G$1" pin="9" pad="9"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:22494/2"/>
</package3dinstances>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="PINHD-1X3" urn="urn:adsk.eagle:component:22524/3" prefix="JP" uservalue="yes" library_version="3">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<gates>
<gate name="A" symbol="PINHD3" x="0" y="0"/>
</gates>
<devices>
<device name="" package="1X03">
<connects>
<connect gate="A" pin="1" pad="1"/>
<connect gate="A" pin="2" pad="2"/>
<connect gate="A" pin="3" pad="3"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:22458/2"/>
</package3dinstances>
<technologies>
<technology name=""/>
</technologies>
</device>
<device name="/90" package="1X03/90">
<connects>
<connect gate="A" pin="1" pad="1"/>
<connect gate="A" pin="2" pad="2"/>
<connect gate="A" pin="3" pad="3"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:22459/2"/>
</package3dinstances>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="PINHD-1X11" urn="urn:adsk.eagle:component:22504/3" prefix="JP" uservalue="yes" library_version="3">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<gates>
<gate name="A" symbol="PINHD11" x="0" y="0"/>
</gates>
<devices>
<device name="" package="1X11">
<connects>
<connect gate="A" pin="1" pad="1"/>
<connect gate="A" pin="10" pad="10"/>
<connect gate="A" pin="11" pad="11"/>
<connect gate="A" pin="2" pad="2"/>
<connect gate="A" pin="3" pad="3"/>
<connect gate="A" pin="4" pad="4"/>
<connect gate="A" pin="5" pad="5"/>
<connect gate="A" pin="6" pad="6"/>
<connect gate="A" pin="7" pad="7"/>
<connect gate="A" pin="8" pad="8"/>
<connect gate="A" pin="9" pad="9"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:22410/2"/>
</package3dinstances>
<technologies>
<technology name=""/>
</technologies>
</device>
<device name="/90" package="1X11/90">
<connects>
<connect gate="A" pin="1" pad="1"/>
<connect gate="A" pin="10" pad="10"/>
<connect gate="A" pin="11" pad="11"/>
<connect gate="A" pin="2" pad="2"/>
<connect gate="A" pin="3" pad="3"/>
<connect gate="A" pin="4" pad="4"/>
<connect gate="A" pin="5" pad="5"/>
<connect gate="A" pin="6" pad="6"/>
<connect gate="A" pin="7" pad="7"/>
<connect gate="A" pin="8" pad="8"/>
<connect gate="A" pin="9" pad="9"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:22416/2"/>
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
<part name="ICE40" library="pinhead" library_urn="urn:adsk.eagle:library:325" deviceset="PINHD-2X17" device="/90" package3d_urn="urn:adsk.eagle:package:22494/2"/>
<part name="BOB" library="con-thomas-betts" library_urn="urn:adsk.eagle:library:191" deviceset="D-SUB25-" device="H2R25RA" package3d_urn="urn:adsk.eagle:package:10573/1"/>
<part name="POWER" library="pinhead" library_urn="urn:adsk.eagle:library:325" deviceset="PINHD-1X3" device="" package3d_urn="urn:adsk.eagle:package:22458/2"/>
<part name="EXT" library="pinhead" library_urn="urn:adsk.eagle:library:325" deviceset="PINHD-1X11" device="" package3d_urn="urn:adsk.eagle:package:22410/2"/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="ICE40" gate="G$1" x="137.16" y="134.62"/>
<instance part="BOB" gate="-1" x="193.04" y="144.78"/>
<instance part="BOB" gate="-2" x="193.04" y="142.24"/>
<instance part="BOB" gate="-3" x="193.04" y="139.7"/>
<instance part="BOB" gate="-4" x="193.04" y="137.16"/>
<instance part="BOB" gate="-5" x="193.04" y="134.62"/>
<instance part="BOB" gate="-6" x="193.04" y="132.08"/>
<instance part="BOB" gate="-7" x="193.04" y="129.54"/>
<instance part="BOB" gate="-8" x="193.04" y="127"/>
<instance part="BOB" gate="-9" x="193.04" y="124.46"/>
<instance part="BOB" gate="-10" x="193.04" y="121.92"/>
<instance part="BOB" gate="-11" x="193.04" y="119.38"/>
<instance part="BOB" gate="-12" x="193.04" y="116.84"/>
<instance part="BOB" gate="-13" x="193.04" y="114.3"/>
<instance part="BOB" gate="-14" x="193.04" y="111.76"/>
<instance part="BOB" gate="-15" x="193.04" y="109.22"/>
<instance part="BOB" gate="-16" x="193.04" y="106.68"/>
<instance part="BOB" gate="-17" x="193.04" y="104.14"/>
<instance part="BOB" gate="-18" x="193.04" y="101.6"/>
<instance part="BOB" gate="-19" x="193.04" y="99.06"/>
<instance part="BOB" gate="-20" x="193.04" y="96.52"/>
<instance part="BOB" gate="-21" x="193.04" y="93.98"/>
<instance part="BOB" gate="-22" x="193.04" y="91.44"/>
<instance part="BOB" gate="-23" x="193.04" y="88.9"/>
<instance part="BOB" gate="-24" x="193.04" y="86.36"/>
<instance part="BOB" gate="-25" x="193.04" y="83.82"/>
<instance part="POWER" gate="A" x="109.22" y="154.94" rot="R180"/>
<instance part="EXT" gate="A" x="109.22" y="121.92" rot="MR0"/>
</instances>
<busses>
</busses>
<nets>
<net name="GND" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="2"/>
<wire x1="142.24" y1="154.94" x2="139.7" y2="154.94" width="0.1524" layer="91"/>
<wire x1="139.7" y1="154.94" x2="139.7" y2="152.4" width="0.1524" layer="91"/>
<pinref part="ICE40" gate="G$1" pin="8"/>
<wire x1="139.7" y1="152.4" x2="139.7" y2="147.32" width="0.1524" layer="91"/>
<wire x1="139.7" y1="147.32" x2="142.24" y2="147.32" width="0.1524" layer="91"/>
<pinref part="ICE40" gate="G$1" pin="4"/>
<wire x1="142.24" y1="152.4" x2="139.7" y2="152.4" width="0.1524" layer="91"/>
<wire x1="139.7" y1="154.94" x2="139.7" y2="165.1" width="0.1524" layer="91"/>
<wire x1="139.7" y1="165.1" x2="165.1" y2="165.1" width="0.1524" layer="91"/>
<label x="160.02" y="165.1" size="1.778" layer="95"/>
<wire x1="127" y1="165.1" x2="139.7" y2="165.1" width="0.1524" layer="91"/>
<junction x="139.7" y="165.1"/>
<junction x="139.7" y="154.94"/>
<junction x="139.7" y="152.4"/>
<pinref part="POWER" gate="A" pin="3"/>
<wire x1="111.76" y1="157.48" x2="127" y2="157.48" width="0.1524" layer="91"/>
<wire x1="127" y1="157.48" x2="127" y2="165.1" width="0.1524" layer="91"/>
</segment>
<segment>
<pinref part="BOB" gate="-18" pin="F"/>
<pinref part="BOB" gate="-19" pin="F"/>
<wire x1="190.5" y1="101.6" x2="190.5" y2="99.06" width="0.1524" layer="91"/>
<pinref part="BOB" gate="-20" pin="F"/>
<wire x1="190.5" y1="99.06" x2="190.5" y2="96.52" width="0.1524" layer="91"/>
<pinref part="BOB" gate="-21" pin="F"/>
<wire x1="190.5" y1="96.52" x2="190.5" y2="93.98" width="0.1524" layer="91"/>
<pinref part="BOB" gate="-22" pin="F"/>
<wire x1="190.5" y1="93.98" x2="190.5" y2="91.44" width="0.1524" layer="91"/>
<pinref part="BOB" gate="-23" pin="F"/>
<wire x1="190.5" y1="91.44" x2="190.5" y2="88.9" width="0.1524" layer="91"/>
<pinref part="BOB" gate="-24" pin="F"/>
<wire x1="190.5" y1="88.9" x2="190.5" y2="86.36" width="0.1524" layer="91"/>
<pinref part="BOB" gate="-25" pin="F"/>
<wire x1="190.5" y1="86.36" x2="190.5" y2="83.82" width="0.1524" layer="91"/>
<wire x1="190.5" y1="83.82" x2="167.64" y2="83.82" width="0.1524" layer="91"/>
<label x="167.64" y="83.82" size="1.778" layer="95"/>
<junction x="190.5" y="83.82"/>
<junction x="190.5" y="86.36"/>
<junction x="190.5" y="88.9"/>
<junction x="190.5" y="91.44"/>
<junction x="190.5" y="93.98"/>
<junction x="190.5" y="96.52"/>
<junction x="190.5" y="99.06"/>
</segment>
</net>
<net name="N$1" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="10"/>
<pinref part="BOB" gate="-1" pin="F"/>
<wire x1="190.5" y1="144.78" x2="142.24" y2="144.78" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$2" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="12"/>
<pinref part="BOB" gate="-2" pin="F"/>
<wire x1="190.5" y1="142.24" x2="142.24" y2="142.24" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$3" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="14"/>
<pinref part="BOB" gate="-3" pin="F"/>
<wire x1="190.5" y1="139.7" x2="142.24" y2="139.7" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$4" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="16"/>
<pinref part="BOB" gate="-4" pin="F"/>
<wire x1="190.5" y1="137.16" x2="142.24" y2="137.16" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$5" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="18"/>
<pinref part="BOB" gate="-5" pin="F"/>
<wire x1="190.5" y1="134.62" x2="142.24" y2="134.62" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$6" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="20"/>
<pinref part="BOB" gate="-6" pin="F"/>
<wire x1="190.5" y1="132.08" x2="142.24" y2="132.08" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$7" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="22"/>
<pinref part="BOB" gate="-7" pin="F"/>
<wire x1="190.5" y1="129.54" x2="142.24" y2="129.54" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$8" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="24"/>
<pinref part="BOB" gate="-8" pin="F"/>
<wire x1="190.5" y1="127" x2="142.24" y2="127" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$9" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="26"/>
<pinref part="BOB" gate="-9" pin="F"/>
<wire x1="190.5" y1="124.46" x2="142.24" y2="124.46" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$10" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="28"/>
<pinref part="BOB" gate="-10" pin="F"/>
<wire x1="190.5" y1="121.92" x2="142.24" y2="121.92" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$11" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="30"/>
<pinref part="BOB" gate="-11" pin="F"/>
<wire x1="190.5" y1="119.38" x2="142.24" y2="119.38" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$12" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="32"/>
<pinref part="BOB" gate="-12" pin="F"/>
<wire x1="190.5" y1="116.84" x2="142.24" y2="116.84" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$13" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="34"/>
<pinref part="BOB" gate="-13" pin="F"/>
<wire x1="190.5" y1="114.3" x2="142.24" y2="114.3" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$16" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="13"/>
<wire x1="134.62" y1="139.7" x2="129.54" y2="139.7" width="0.1524" layer="91"/>
<wire x1="129.54" y1="139.7" x2="129.54" y2="106.68" width="0.1524" layer="91"/>
<pinref part="BOB" gate="-16" pin="F"/>
<wire x1="129.54" y1="106.68" x2="190.5" y2="106.68" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$17" class="0">
<segment>
<pinref part="BOB" gate="-17" pin="F"/>
<wire x1="190.5" y1="104.14" x2="132.08" y2="104.14" width="0.1524" layer="91"/>
<wire x1="132.08" y1="104.14" x2="132.08" y2="137.16" width="0.1524" layer="91"/>
<pinref part="ICE40" gate="G$1" pin="15"/>
<wire x1="132.08" y1="137.16" x2="134.62" y2="137.16" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$18" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="17"/>
<pinref part="EXT" gate="A" pin="1"/>
<wire x1="111.76" y1="134.62" x2="134.62" y2="134.62" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$19" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="19"/>
<pinref part="EXT" gate="A" pin="2"/>
<wire x1="111.76" y1="132.08" x2="134.62" y2="132.08" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$20" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="21"/>
<pinref part="EXT" gate="A" pin="3"/>
<wire x1="111.76" y1="129.54" x2="134.62" y2="129.54" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$21" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="23"/>
<pinref part="EXT" gate="A" pin="4"/>
<wire x1="111.76" y1="127" x2="134.62" y2="127" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$22" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="25"/>
<pinref part="EXT" gate="A" pin="5"/>
<wire x1="111.76" y1="124.46" x2="134.62" y2="124.46" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$23" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="27"/>
<pinref part="EXT" gate="A" pin="6"/>
<wire x1="111.76" y1="121.92" x2="134.62" y2="121.92" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$24" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="29"/>
<pinref part="EXT" gate="A" pin="7"/>
<wire x1="111.76" y1="119.38" x2="134.62" y2="119.38" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$25" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="31"/>
<pinref part="EXT" gate="A" pin="8"/>
<wire x1="111.76" y1="116.84" x2="134.62" y2="116.84" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$26" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="33"/>
<pinref part="EXT" gate="A" pin="9"/>
<wire x1="111.76" y1="114.3" x2="134.62" y2="114.3" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$27" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="9"/>
<wire x1="124.46" y1="111.76" x2="124.46" y2="144.78" width="0.1524" layer="91"/>
<wire x1="124.46" y1="144.78" x2="134.62" y2="144.78" width="0.1524" layer="91"/>
<pinref part="BOB" gate="-14" pin="F"/>
<wire x1="124.46" y1="111.76" x2="190.5" y2="111.76" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$14" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="11"/>
<wire x1="127" y1="109.22" x2="127" y2="142.24" width="0.1524" layer="91"/>
<wire x1="127" y1="142.24" x2="134.62" y2="142.24" width="0.1524" layer="91"/>
<pinref part="BOB" gate="-15" pin="F"/>
<wire x1="190.5" y1="109.22" x2="127" y2="109.22" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$29" class="0">
<segment>
<pinref part="EXT" gate="A" pin="10"/>
<wire x1="111.76" y1="111.76" x2="116.84" y2="111.76" width="0.1524" layer="91"/>
<wire x1="116.84" y1="111.76" x2="116.84" y2="147.32" width="0.1524" layer="91"/>
<pinref part="ICE40" gate="G$1" pin="7"/>
<wire x1="116.84" y1="147.32" x2="134.62" y2="147.32" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$30" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="5"/>
<wire x1="134.62" y1="149.86" x2="119.38" y2="149.86" width="0.1524" layer="91"/>
<pinref part="EXT" gate="A" pin="11"/>
<wire x1="119.38" y1="149.86" x2="119.38" y2="109.22" width="0.1524" layer="91"/>
<wire x1="119.38" y1="109.22" x2="111.76" y2="109.22" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$15" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="3"/>
<pinref part="POWER" gate="A" pin="1"/>
<wire x1="111.76" y1="152.4" x2="134.62" y2="152.4" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$28" class="0">
<segment>
<pinref part="ICE40" gate="G$1" pin="1"/>
<pinref part="POWER" gate="A" pin="2"/>
<wire x1="111.76" y1="154.94" x2="134.62" y2="154.94" width="0.1524" layer="91"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
<errors>
<approved hash="111,1,139.7,149.86,GND,,,,,"/>
<approved hash="113,1,138.388,136.116,ICE40,,,,,"/>
<approved hash="113,1,108.223,156.436,POWER,,,,,"/>
<approved hash="113,1,111.523,123.416,EXT,,,,,"/>
</errors>
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
