import unittest
import apc

class TestFTest(unittest.TestCase):

    def test_VNJ(self):
        model = apc.Model()
        model.data_from_df(apc.loss_VNJ(), data_format='CL')
        model.fit('log_normal_response', 'AC')
        sub_models = [model.sub_model(coh_from_to=(1,5)), 
                      model.sub_model(coh_from_to=(6,10))]
        f = apc.f_test(model, sub_models)
        self.assertEqual(round(f['F_stat'], 3), 0.242)
        self.assertEqual(round(f['p_value'], 3), 0.912)

    def test_BZ(self):
        model = apc.Model()
        model.data_from_df(apc.loss_BZ(), data_format='CL')
        model.fit('od_poisson_response', 'APC')
        sub_models = [model.sub_model(per_from_to=(1977,1981)),
                      model.sub_model(per_from_to=(1982,1984)),
                      model.sub_model(per_from_to=(1985,1987))]
        f = apc.f_test(model, sub_models)
        self.assertEqual(round(f['F_stat'], 3), 1.855)
        self.assertEqual(round(f['p_value'], 3), 0.133)
        
if __name__ == '__main__':
    unittest.main()