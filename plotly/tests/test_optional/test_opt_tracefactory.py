from unittest import TestCase
from plotly.graph_objs import graph_objs, Line
from plotly.exceptions import PlotlyError

import plotly.tools as tls
import math
from nose.tools import raises

import numpy as np


class TestStreamline(TestCase):

    def test_wrong_arrow_scale(self):

        # check for ValueError if arrow_scale is <= 0

        kwargs = {'x': [0, 2], 'y': [0, 2],
                  'u': [[-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]],
                  'arrow_scale': 0}
        self.assertRaises(ValueError, tls.TraceFactory.create_streamline,
                          **kwargs)

    def test_wrong_density(self):

        # check for ValueError if density is <= 0

        kwargs = {'x': [0, 2], 'y': [0, 2],
                  'u': [[-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]],
                  'density': 0}
        self.assertRaises(ValueError, tls.TraceFactory.create_streamline,
                          **kwargs)

    def test_uneven_x(self):

        # check for PlotlyError if x is not evenly spaced

        kwargs = {'x': [0, 2, 7, 9], 'y': [0, 2, 4, 6],
                  'u': [[-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]]}
        self.assertRaises(PlotlyError, tls.TraceFactory.create_streamline,
                          **kwargs)

    def test_uneven_y(self):

        # check for PlotlyError if y is not evenly spaced

        kwargs = {'x': [0, 2, 4, 6], 'y': [1.5, 2, 3, 3.5],
                  'u': [[-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]]}
        self.assertRaises(PlotlyError, tls.TraceFactory.create_streamline,
                          **kwargs)

    def test_unequal_shape_u(self):

        # check for PlotlyError if u and v are not the same length

        kwargs = {'x': [0, 2, 4, 6], 'y': [1.5, 2, 3, 3.5],
                  'u': [[-1, -5], [-1, -5], [-1, -5]],
                  'v': [[1, 1], [-3, -3]]}
        self.assertRaises(PlotlyError, tls.TraceFactory.create_streamline,
                          **kwargs)

    def test_simple_streamline(self):

        # Need np to check streamline data,
        # this checks that the first 101 x and y values from streamline are
        # what we expect for a simple streamline where:
        # x = np.linspace(-1, 1, 3)
        # y = np.linspace(-1, 1, 3)
        # Y, X = np.meshgrid(x, y)
        # u = X**2
        # v = Y**2
        # u = u.T #transpose
        # v = v.T #transpose

        strmln = tls.TraceFactory.create_streamline(x=[-1., 0., 1.],
                                                    y=[-1., 0., 1.],
                                                    u=[[1., 0., 1.],
                                                       [1., 0., 1.],
                                                       [1., 0., 1.]],
                                                    v=[[1., 1., 1.],
                                                       [0., 0., 0.],
                                                       [1., 1., 1.]])
        expected_strmln_0_100 = {
            'y': [-1.0, -0.9788791845863757, -0.9579399744939614, -0.9371777642073374, -0.9165881396413338, -0.8961668671832106, -0.8759098835283448, -0.8558132862403048, -0.835873324973195, -0.8160863933003534, -0.7964490210989816, -0.7769578674451656, -0.7576097139780906, -0.7384014586961288, -0.7193301101509343, -0.7003927820087748, -0.681586687951103, -0.6629091368888596, -0.64435752846723, -0.6259293488396024, -0.6076221666912738, -0.5894336294951057, -0.5713614599827976, -0.5534034528167977, -0.5355574714490806, -0.5178214451541254, -0.5001933662244311, -0.4826712873178177, -0.4652533189465894, -0.44793762709939944, -0.4307224309873414, -0.4136060009064273, -0.39658665620919065, -0.3796627633786812, -0.3628327341986042, -0.34609502401380254, -0.3294481300756896, -0.31289058996761565, -0.2964209801054992, -0.28003791430937197, -0.2637400424417804, -0.24752604910925968, -0.23139465242334434, -0.21534460281781365, -0.19937468191908325, -0.18348370146685278, -0.1676705022823033, -0.15193395328130999, -0.13627295053029143, -0.1206864163424669, -0.10517329841242584, -0.08973256898704507, -0.07436322407090357, -0.05906428266445696, -0.04383478603333624, -0.028673797007230273, -0.013580399306900914, 0.0014484211645073852, 0.01648792568956914, 0.03159429687713278, 0.04676843461935776, 0.062011259175942746, 0.07732371182540754, 0.09270675554339824, 0.10816137570939799, 0.12368858084331191, 0.1392894033734846, 0.1549649004378033, 0.1707161547196483, 0.1865442753205595, 0.20245039867161063, 0.21843568948560943, 0.23450134175238246, 0.25064857977955146, 0.26687865928136767, 0.2831928685183458, 0.29959252949062387, 0.3160789991881776, 0.33265367090123643, 0.3493179755944802, 0.366073383348855, 0.3829214048751186, 0.39986359310352526, 0.41690154485438513, 0.4340369025945845, 0.4512713562855355, 0.46860664532844054, 0.4860445606132082, 0.5035869466778524, 0.5212357039857456, 0.5389927913286829, 0.5568602283643591, 0.5748400982975623, 0.5929345507151613, 0.6111458045858065, 0.6294761514361948, 0.6479279587167714, 0.6665036733708583, 0.6852058256224467, 0.704037032999252],
            'x': [-1.0, -0.9788791845863756, -0.9579399744939614, -0.9371777642073374, -0.9165881396413338, -0.8961668671832106, -0.8759098835283448, -0.8558132862403048, -0.835873324973195, -0.8160863933003534, -0.7964490210989816, -0.7769578674451656, -0.7576097139780906, -0.7384014586961289, -0.7193301101509344, -0.7003927820087748, -0.6815866879511031, -0.6629091368888596, -0.6443575284672302, -0.6259293488396025, -0.6076221666912739, -0.5894336294951058, -0.5713614599827976, -0.5534034528167978, -0.5355574714490807, -0.5178214451541254, -0.5001933662244312, -0.4826712873178177, -0.4652533189465894, -0.44793762709939944, -0.4307224309873414, -0.4136060009064273, -0.39658665620919065, -0.3796627633786812, -0.3628327341986042, -0.34609502401380254, -0.3294481300756896, -0.31289058996761565, -0.2964209801054992, -0.28003791430937197, -0.2637400424417804, -0.24752604910925968, -0.23139465242334434, -0.21534460281781365, -0.19937468191908325, -0.18348370146685278, -0.1676705022823033, -0.15193395328130999, -0.13627295053029143, -0.1206864163424669, -0.10517329841242584, -0.08973256898704507, -0.07436322407090357, -0.05906428266445696, -0.04383478603333624, -0.028673797007230273, -0.013580399306900914, 0.0014484211645073852, 0.01648792568956914, 0.03159429687713278, 0.04676843461935776, 0.062011259175942746, 0.07732371182540754, 0.09270675554339824, 0.10816137570939799, 0.12368858084331191, 0.1392894033734846, 0.1549649004378033, 0.1707161547196483, 0.1865442753205595, 0.20245039867161063, 0.21843568948560943, 0.23450134175238246, 0.25064857977955146, 0.26687865928136767, 0.2831928685183458, 0.29959252949062387, 0.3160789991881776, 0.33265367090123643, 0.3493179755944802, 0.366073383348855, 0.3829214048751186, 0.39986359310352526, 0.41690154485438513, 0.4340369025945845, 0.4512713562855355, 0.46860664532844054, 0.4860445606132082, 0.5035869466778524, 0.5212357039857456, 0.5389927913286829, 0.5568602283643591, 0.5748400982975623, 0.5929345507151613, 0.6111458045858065, 0.6294761514361948, 0.6479279587167714, 0.6665036733708583, 0.6852058256224467, 0.704037032999252],
            'type': 'scatter',
            'mode': 'lines'
        }
        self.assertAlmostEqual(strmln['y'][0:100], expected_strmln_0_100['y'])
        self.assertAlmostEqual(strmln['x'][0:100], expected_strmln_0_100['x'])

    def test_numpy_streamline(self):

        # check that streamline results as expected when x, y, u and v are
        # defined with numpy (typical use)

        x = np.linspace(-3, 3, 100)
        y = np.linspace(-3, 3, 100)
        Y, X = np.meshgrid(x, y)
        u = -1 - X**2 + Y
        v = 1 + X - Y**2
        streamline = tls.TraceFactory.create_streamline(x, y, u, v,
                                                        arrow_scale=.1,
                                                        density=3)
        expected_streamline = {
            'y': [0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393049198, 0.0018922002393044757, 0.0018922002393040316, 0.0018922002393022552, 0.0018922002392969262, 0.001892200239281383, 0.0018922002392334214, 0.0018922002390828752, 0.001892200238609476, 0.0018922002371390967, 0.0018922002325685305, 0.001892200218438056, 0.0018922001749084316, 0.0018922000414152151, 0.0018921996341290104, 0.0018921983989277358, 0.0018921946791010669, 0.0018921835702832013, 0.0018921507305122987, 0.0018920548629908218, 0.0018917794342634409, 0.0018910045248765606, 0.0018888860033485777, 0.001883330861293775, 0.00186969877142662, 0.0018400887882492611, 0.001792611800322419, 0.0017993604930395257, 0.0023459865813966196, 0.005768713743637743, 0.02122353426458945, 0.049323537523347394, 0.07755934266944609],
            'x': [1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645543, 1.000918273645544, 1.0009182736455449, 1.0009182736455466, 1.0009182736455546, 1.0009182736455813, 1.00091827364567, 1.0009182736459632, 1.0009182736469233, 1.00091827365008, 1.0009182736604547, 1.000918273694551, 1.000918273806616, 1.000918274174933, 1.0009182753854606, 1.0009182793640328, 1.0009182924401863, 1.000918335416853, 1.0009184766659116, 1.0009189409018102, 1.000920466685284, 1.000925481451195, 1.0009419639631494, 1.0009961490137123, 1.0011745163431298, 1.0017672338974037, 1.0039090426442545, 1.0110879873093834, 1.0202616741544626],
            'type': 'scatter',
            'mode': 'lines'
        }
        self.assertAlmostEqual(streamline['y'][0:100], expected_streamline['y'])
        self.assertAlmostEqual(streamline['x'][0:100], expected_streamline['x'])
