#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: ece_1896_STARR_FM_TX
# Author: adam-nichols
# GNU Radio version: 3.10.11.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import iio
import sip
import threading



class ece_1896_STARR_FM_TX(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "ece_1896_STARR_FM_TX", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("ece_1896_STARR_FM_TX")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "ece_1896_STARR_FM_TX")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.carrier_freq = carrier_freq = int(147.540e6)
        self.audio_samp_rate = audio_samp_rate = 48000
        self.atten = atten = 10
        self.RF_samp_rate = RF_samp_rate = 480000

        ##################################################
        # Blocks
        ##################################################

        self._atten_range = qtgui.Range(0, 89.7, 0.1, 10, 200)
        self._atten_win = qtgui.RangeWidget(self._atten_range, self.set_atten, "'atten'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._atten_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
            1024, #size
            audio_samp_rate, #samp_rate
            "Audio", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['Signal 1', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.iio_pluto_sink_0 = iio.fmcomms2_sink_fc32('ip:192.168.2.20' if 'ip:192.168.2.20' else iio.get_pluto_uri(), [True, True], 32768, False)
        self.iio_pluto_sink_0.set_len_tag_key('')
        self.iio_pluto_sink_0.set_bandwidth(20000000)
        self.iio_pluto_sink_0.set_frequency(carrier_freq)
        self.iio_pluto_sink_0.set_samplerate(RF_samp_rate)
        self.iio_pluto_sink_0.set_attenuation(0, atten)
        self.iio_pluto_sink_0.set_filter_params('Auto', '', 0, 0)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('/home/adam-nichols/Documents/Pitt/ECE 1896/ECE1472 Lab1 speech files/Fessenden_long_clip_fs48000_mono.wav', True)
        self.analog_nbfm_tx_0 = analog.nbfm_tx(
        	audio_rate=audio_samp_rate,
        	quad_rate=RF_samp_rate,
        	tau=(75e-6),
        	max_dev=5e3,
        	fh=(-1.0),
                )


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_nbfm_tx_0, 0), (self.iio_pluto_sink_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.analog_nbfm_tx_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.qtgui_time_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "ece_1896_STARR_FM_TX")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_carrier_freq(self):
        return self.carrier_freq

    def set_carrier_freq(self, carrier_freq):
        self.carrier_freq = carrier_freq
        self.iio_pluto_sink_0.set_frequency(self.carrier_freq)

    def get_audio_samp_rate(self):
        return self.audio_samp_rate

    def set_audio_samp_rate(self, audio_samp_rate):
        self.audio_samp_rate = audio_samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.audio_samp_rate)

    def get_atten(self):
        return self.atten

    def set_atten(self, atten):
        self.atten = atten
        self.iio_pluto_sink_0.set_attenuation(0,self.atten)

    def get_RF_samp_rate(self):
        return self.RF_samp_rate

    def set_RF_samp_rate(self, RF_samp_rate):
        self.RF_samp_rate = RF_samp_rate
        self.iio_pluto_sink_0.set_samplerate(self.RF_samp_rate)




def main(top_block_cls=ece_1896_STARR_FM_TX, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
