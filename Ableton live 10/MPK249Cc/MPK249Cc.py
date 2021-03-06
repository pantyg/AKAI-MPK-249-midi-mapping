# MPK249Cc


from __future__ import with_statement
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.Layer import Layer
from _Framework.InputControlElement import MIDI_CC_TYPE
from _Framework.SliderElement import SliderElement
from _Framework.EncoderElement import EncoderElement
from _Framework.ButtonElement import ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.MixerComponent import MixerComponent
from _Framework.DeviceComponent import DeviceComponent
from _Framework.TransportComponent import TransportComponent
from _Framework.DrumRackComponent import DrumRackComponent
from _Framework.SessionComponent import SessionComponent
from _Framework.MidiMap import MidiMap as MidiMapBase
from _Framework.MidiMap import make_button, make_encoder, make_slider
from _Framework.InputControlElement import MIDI_NOTE_TYPE, MIDI_CC_TYPE

# Relative Knobs
def make_encoder(name, channel, number, midi_message_type):
 return EncoderElement(midi_message_type, channel, number, Live.MidiMap.MapMode.relative_two_compliment, name=name)

class MidiMap(MidiMapBase):

    def __init__(self, *a, **k):
        super(MidiMap, self).__init__(*a, **k)
        self.add_button('Play', 0, 118, MIDI_CC_TYPE)
        self.add_button('Record', 0, 119, MIDI_CC_TYPE)
        self.add_button('Stop', 0, 117, MIDI_CC_TYPE)
        self.add_button('Loop', 0, 114, MIDI_CC_TYPE)
        self.add_button('Forward', 0, 116, MIDI_CC_TYPE)
        self.add_button('Backward', 0, 115, MIDI_CC_TYPE)
        self.add_matrix('Encoders', make_encoder, 0, [[22, 23, 24, 25, 26,  27, 28, 29]], MIDI_CC_TYPE)
        self.add_matrix('Drum_Pads', make_button, 1, [[81, 83, 84, 86],[74, 76, 77, 79], [67, 69, 71, 72],[60, 62, 64, 65]], MIDI_NOTE_TYPE)

class MPK249Cc(ControlSurface):

    def __init__(self, *a, **k):
        super(MPK249Cc, self).__init__(*a, **k)
        self.show_message("^^MPK249Cc")
        self.log_message("^^MPK249Cc")
        with self.component_guard():
            midimap = MidiMap()
            #buttons and faders 
            #Bank A - Channel 1 
            self._Encoder0 = EncoderElement(MIDI_CC_TYPE,1,22, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder0')
            self._Encoder1 = EncoderElement(MIDI_CC_TYPE,1,23, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder1')
            self._Encoder2 = EncoderElement(MIDI_CC_TYPE,1,24, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder2')
            self._Encoder3 = EncoderElement(MIDI_CC_TYPE,1,25, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder3')
            self._Encoder4 = EncoderElement(MIDI_CC_TYPE,1,26, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder4')
            self._Encoder5 = EncoderElement(MIDI_CC_TYPE,1,27, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder5')
            self._Encoder6 = EncoderElement(MIDI_CC_TYPE,1,28, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder6')
            self._Encoder7 = EncoderElement(MIDI_CC_TYPE,1,29, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder7')
            self._ArmButton0 = ButtonElement(False, MIDI_CC_TYPE, 0, 32, name='ArmButton0')
            self._ArmButton1 = ButtonElement(False, MIDI_CC_TYPE, 0, 33, name='ArmButton1')
            self._ArmButton2 = ButtonElement(False, MIDI_CC_TYPE, 0, 34, name='ArmButton2')
            self._ArmButton3 = ButtonElement(False, MIDI_CC_TYPE, 0, 35, name='ArmButton3')
            self._ArmButton4 = ButtonElement(False, MIDI_CC_TYPE, 0, 36, name='ArmButton4')
            self._ArmButton5 = ButtonElement(False, MIDI_CC_TYPE, 0, 37, name='ArmButton5')
            self._ArmButton6 = ButtonElement(False, MIDI_CC_TYPE, 0, 38, name='ArmButton6')
            self._ArmButton7 = ButtonElement(False, MIDI_CC_TYPE, 0, 39, name='ArmButton7')
            self._VolumeSlider0 = SliderElement(MIDI_CC_TYPE, 0, 12, name='VolumeSlider0')
            self._VolumeSlider1 = SliderElement(MIDI_CC_TYPE, 0, 13, name='VolumeSlider1')
            self._VolumeSlider2 = SliderElement(MIDI_CC_TYPE, 0, 14, name='VolumeSlider2')
            self._VolumeSlider3 = SliderElement(MIDI_CC_TYPE, 0, 15, name='VolumeSlider3')
            self._VolumeSlider4 = SliderElement(MIDI_CC_TYPE, 0, 16, name='VolumeSlider4')
            self._VolumeSlider5 = SliderElement(MIDI_CC_TYPE, 0, 17, name='VolumeSlider5')
            self._VolumeSlider6 = SliderElement(MIDI_CC_TYPE, 0, 18, name='VolumeSlider6')
            self._VolumeSlider7 = SliderElement(MIDI_CC_TYPE, 0, 19, name='VolumeSlider7')
            #Bank B - Channel 2
            self._Encoder8 = EncoderElement(MIDI_CC_TYPE,2,22, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder8')
            self._Encoder9 = EncoderElement(MIDI_CC_TYPE,2,23, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder9')
            self._Encoder10 = EncoderElement(MIDI_CC_TYPE,2,24, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder10')
            self._Encoder11 = EncoderElement(MIDI_CC_TYPE,2,25, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder11')
            self._Encoder12 = EncoderElement(MIDI_CC_TYPE,2,26, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder12')
            self._Encoder13 = EncoderElement(MIDI_CC_TYPE,2,27, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder13')
            self._Encoder14 = EncoderElement(MIDI_CC_TYPE,2,28, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder14')
            self._Encoder15 = EncoderElement(MIDI_CC_TYPE,2,29, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder15')
            self._ArmButton8 = ButtonElement(False, MIDI_CC_TYPE, 1, 32, name='ArmButton8')
            self._ArmButton9 = ButtonElement(False, MIDI_CC_TYPE, 1, 33, name='ArmButton9')
            self._ArmButton10 = ButtonElement(False, MIDI_CC_TYPE, 1, 34, name='ArmButton10')
            self._ArmButton11 = ButtonElement(False, MIDI_CC_TYPE, 1, 35, name='ArmButton11')
            self._ArmButton12 = ButtonElement(False, MIDI_CC_TYPE, 1, 36, name='ArmButton12')
            self._ArmButton13 = ButtonElement(False, MIDI_CC_TYPE, 1, 37, name='ArmButton13')
            self._ArmButton14 = ButtonElement(False, MIDI_CC_TYPE, 1, 38, name='ArmButton14')
            self._ArmButton15 = ButtonElement(False, MIDI_CC_TYPE, 1, 39, name='ArmButton15')
            self._VolumeSlider8 = SliderElement(MIDI_CC_TYPE, 1, 12, name='VolumeSlider8')
            self._VolumeSlider9 = SliderElement(MIDI_CC_TYPE, 1, 13, name='VolumeSlider9')
            self._VolumeSlider10 = SliderElement(MIDI_CC_TYPE, 1, 14, name='VolumeSlider10')
            self._VolumeSlider11 = SliderElement(MIDI_CC_TYPE, 1, 15, name='VolumeSlider11')
            self._VolumeSlider12 = SliderElement(MIDI_CC_TYPE, 1, 16, name='VolumeSlider12')
            self._VolumeSlider13 = SliderElement(MIDI_CC_TYPE, 1, 17, name='VolumeSlider13')
            self._VolumeSlider14 = SliderElement(MIDI_CC_TYPE, 1, 18, name='VolumeSlider14')
            self._VolumeSlider15 = SliderElement(MIDI_CC_TYPE, 1, 19, name='VolumeSlider15')
            #Bank C - Channel 3 
            self._Encoder16 = EncoderElement(MIDI_CC_TYPE,3,22, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder16')
            self._Encoder17 = EncoderElement(MIDI_CC_TYPE,3,23, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder17')
            self._Encoder18 = EncoderElement(MIDI_CC_TYPE,3,24, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder18')
            self._Encoder19 = EncoderElement(MIDI_CC_TYPE,3,25, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder19')
            self._Encoder20 = EncoderElement(MIDI_CC_TYPE,3,26, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder20')
            self._Encoder21 = EncoderElement(MIDI_CC_TYPE,3,27, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder21')
            self._Encoder22 = EncoderElement(MIDI_CC_TYPE,3,28, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder22')
            self._Encoder23 = EncoderElement(MIDI_CC_TYPE,3,29, Live.MidiMap.MapMode.relative_two_compliment, name='Encoder23')
            self._ArmButton16 = ButtonElement(False, MIDI_CC_TYPE, 2, 32, name='ArmButton16')
            self._ArmButton17 = ButtonElement(False, MIDI_CC_TYPE, 2, 33, name='ArmButton17')
            self._ArmButton18 = ButtonElement(False, MIDI_CC_TYPE, 2, 34, name='ArmButton18')
            self._ArmButton19 = ButtonElement(False, MIDI_CC_TYPE, 2, 35, name='ArmButton19')
            self._ArmButton20 = ButtonElement(False, MIDI_CC_TYPE, 2, 36, name='ArmButton20')
            self._ArmButton21 = ButtonElement(False, MIDI_CC_TYPE, 2, 37, name='ArmButton21')
            self._ArmButton22 = ButtonElement(False, MIDI_CC_TYPE, 2, 38, name='ArmButton22')
            self._ArmButton23 = ButtonElement(False, MIDI_CC_TYPE, 2, 39, name='ArmButton23')
            self._VolumeSlider16 = SliderElement(MIDI_CC_TYPE, 2, 12, name='VolumeSlider16')
            self._VolumeSlider17 = SliderElement(MIDI_CC_TYPE, 2, 13, name='VolumeSlider17')
            self._VolumeSlider18 = SliderElement(MIDI_CC_TYPE, 2, 14, name='VolumeSlider18')
            self._VolumeSlider19 = SliderElement(MIDI_CC_TYPE, 2, 15, name='VolumeSlider19')
            self._VolumeSlider20 = SliderElement(MIDI_CC_TYPE, 2, 16, name='VolumeSlider20')
            self._VolumeSlider21 = SliderElement(MIDI_CC_TYPE, 2, 17, name='VolumeSlider21')
            self._VolumeSlider22 = SliderElement(MIDI_CC_TYPE, 2, 18, name='VolumeSlider22')
            self._VolumeSlider23 = SliderElement(MIDI_CC_TYPE, 2, 19, name='VolumeSlider23')
            #Drums
            drum_rack = DrumRackComponent(name='Drum_Rack', is_enabled=False, layer=Layer(pads=midimap['Drum_Pads']))
            drum_rack.set_enabled(True)
            #Transport
            transport = TransportComponent(name='Transport', is_enabled=False, layer=Layer(play_button=midimap['Play'], record_button=midimap['Record'], stop_button=midimap['Stop'], seek_forward_button=midimap['Forward'], seek_backward_button=midimap['Backward'], loop_button=midimap['Loop']))
            transport.set_enabled(True)
            #Device
            self._device = DeviceComponent(name='Device', is_enabled=False, layer=Layer(parameter_controls=midimap['Encoders']), device_selection_follows_track_selection=True)
            self._device.set_enabled(True)
            self.set_device_component(self._device)
            #Mixer
            mixer_size = 24
            self._mixer = MixerComponent(mixer_size, name='Mixer', is_enabled=False)
            #Mixer Console
            #Bank A
            self._mixer.channel_strip(0).layer = Layer(volume_control = self._VolumeSlider0, arm_button=self._ArmButton0, pan_control=self._Encoder0)
            self._mixer.channel_strip(1).layer = Layer(volume_control = self._VolumeSlider1, arm_button=self._ArmButton1, pan_control=self._Encoder1)
            self._mixer.channel_strip(2).layer = Layer(volume_control = self._VolumeSlider2, arm_button=self._ArmButton2, pan_control=self._Encoder2)
            self._mixer.channel_strip(3).layer = Layer(volume_control = self._VolumeSlider3, arm_button=self._ArmButton3, pan_control=self._Encoder3)
            self._mixer.channel_strip(4).layer = Layer(volume_control = self._VolumeSlider4, arm_button=self._ArmButton4, pan_control=self._Encoder4)
            self._mixer.channel_strip(5).layer = Layer(volume_control = self._VolumeSlider5, arm_button=self._ArmButton5, pan_control=self._Encoder5)
            self._mixer.channel_strip(6).layer = Layer(volume_control = self._VolumeSlider6, arm_button=self._ArmButton6, pan_control=self._Encoder6)
            self._mixer.channel_strip(7).layer = Layer(volume_control = self._VolumeSlider7, arm_button=self._ArmButton7, pan_control=self._Encoder7)
            #Bank B
            self._mixer.channel_strip(8).layer = Layer(volume_control = self._VolumeSlider8, arm_button=self._ArmButton8, pan_control=self._Encoder8)
            self._mixer.channel_strip(9).layer = Layer(volume_control = self._VolumeSlider9, arm_button=self._ArmButton9, pan_control=self._Encoder9)
            self._mixer.channel_strip(10).layer = Layer(volume_control = self._VolumeSlider10, arm_button=self._ArmButton10, pan_control=self._Encoder10)
            self._mixer.channel_strip(11).layer = Layer(volume_control = self._VolumeSlider11, arm_button=self._ArmButton11, pan_control=self._Encoder11)
            self._mixer.channel_strip(12).layer = Layer(volume_control = self._VolumeSlider12, arm_button=self._ArmButton12, pan_control=self._Encoder12)
            self._mixer.channel_strip(13).layer = Layer(volume_control = self._VolumeSlider13, arm_button=self._ArmButton13, pan_control=self._Encoder13)
            self._mixer.channel_strip(14).layer = Layer(volume_control = self._VolumeSlider14, arm_button=self._ArmButton14, pan_control=self._Encoder14)
            self._mixer.channel_strip(15).layer = Layer(volume_control = self._VolumeSlider15, arm_button=self._ArmButton15, pan_control=self._Encoder15)
            #Bank C     
            self._mixer.channel_strip(16).layer = Layer(volume_control = self._VolumeSlider16, arm_button=self._ArmButton16, pan_control=self._Encoder16)
            self._mixer.channel_strip(17).layer = Layer(volume_control = self._VolumeSlider17, arm_button=self._ArmButton17, pan_control=self._Encoder17)
            self._mixer.channel_strip(18).layer = Layer(volume_control = self._VolumeSlider18, arm_button=self._ArmButton18, pan_control=self._Encoder18)
            self._mixer.channel_strip(19).layer = Layer(volume_control = self._VolumeSlider19, arm_button=self._ArmButton19, pan_control=self._Encoder19)
            self._mixer.channel_strip(20).layer = Layer(volume_control = self._VolumeSlider20, arm_button=self._ArmButton20, pan_control=self._Encoder20)
            self._mixer.channel_strip(21).layer = Layer(volume_control = self._VolumeSlider21, arm_button=self._ArmButton21, pan_control=self._Encoder21)
            self._mixer.channel_strip(22).layer = Layer(volume_control = self._VolumeSlider22, arm_button=self._ArmButton22, pan_control=self._Encoder22)
            self._mixer.channel_strip(23).layer = Layer(volume_control = self._VolumeSlider23, arm_button=self._ArmButton23, pan_control=self._Encoder23)
            self._mixer.set_enabled(True)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
