#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Mode S Ppm Usrpb210 File Sink
# Generated: Sat Jan  1 21:44:46 2022
##################################################


from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import adsb
import time


class Mode_S_PPM_USRPB210_File_Sink(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Mode S Ppm Usrpb210 File Sink")

        ##################################################
        # Variables
        ##################################################
        self.serial = serial = "False"
        self.samp_rate = samp_rate = 2e6
        self.notes = notes = "Decodes ADSB messages and prints the output to stdout and to a file."
        self.gain = gain = 70
        self.freq = freq = 1090e6
        self.filepath = filepath = "/home/user/FISSURE/Attack Recordings/adsb1.bin"
        self.channel = channel = "A:A"
        self.antenna = antenna = "TX/RX"

        ##################################################
        # Message Queues
        ##################################################
        adsb_decoder_0_msgq_out = blocks_message_source_0_msgq_in = gr.msg_queue(2)
        adsb_framer_0_msgq_out = adsb_decoder_0_msgq_in = gr.msg_queue(2)

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join((serial, "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_subdev_spec(channel, 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(freq, 0)
        self.uhd_usrp_source_0.set_gain(gain, 0)
        self.uhd_usrp_source_0.set_antenna(antenna, 0)
        self.digital_correlate_access_code_tag_bb_0 = digital.correlate_access_code_tag_bb('1010000101000000', 0, 'adsb_preamble')
        self.blocks_threshold_ff_0 = blocks.threshold_ff(0.01, 0.01, 0)
        self.blocks_message_source_0 = blocks.message_source(gr.sizeof_char*1, blocks_message_source_0_msgq_in)
        self.blocks_float_to_uchar_0 = blocks.float_to_uchar()
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, filepath, True)
        self.blocks_file_sink_0_0.set_unbuffered(True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/dev/stdout', True)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.adsb_framer_0 = adsb.framer(tx_msgq=adsb_framer_0_msgq_out)
        self.adsb_decoder_0 = adsb.decoder(rx_msgq=adsb_decoder_0_msgq_in,tx_msgq=adsb_decoder_0_msgq_out,output_type="csv",check_parity=True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.blocks_float_to_uchar_0, 0), (self.digital_correlate_access_code_tag_bb_0, 0))
        self.connect((self.blocks_message_source_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_message_source_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_threshold_ff_0, 0), (self.blocks_float_to_uchar_0, 0))
        self.connect((self.digital_correlate_access_code_tag_bb_0, 0), (self.adsb_framer_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_complex_to_mag_squared_0, 0))

    def get_serial(self):
        return self.serial

    def set_serial(self, serial):
        self.serial = serial

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_notes(self):
        return self.notes

    def set_notes(self, notes):
        self.notes = notes

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.uhd_usrp_source_0.set_gain(self.gain, 0)


    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.uhd_usrp_source_0.set_center_freq(self.freq, 0)

    def get_filepath(self):
        return self.filepath

    def set_filepath(self, filepath):
        self.filepath = filepath
        self.blocks_file_sink_0_0.open(self.filepath)

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel

    def get_antenna(self):
        return self.antenna

    def set_antenna(self, antenna):
        self.antenna = antenna
        self.uhd_usrp_source_0.set_antenna(self.antenna, 0)


def main(top_block_cls=Mode_S_PPM_USRPB210_File_Sink, options=None):

    tb = top_block_cls()
    tb.start()
    tb.wait()


if __name__ == '__main__':
    main()
