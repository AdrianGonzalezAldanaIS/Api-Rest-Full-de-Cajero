import pytest
#from dao.TarjetaDAO import TarjetaDao
import datetime
from decimal import Decimal
from exceptions.TipoDatoException import TipoDatoException
from dao.TarjetaDAO import TarjetaDao


class TestQuerysTarjeta:
    
    #------------- Preubas unitarias de limites ---------------------
    """
    ---------------- Pruebas para consulta_tarjeta ------------------
    """
    #------------- Pruebas unitaria para parametros validos ---------
    
    @pytest.mark.parametrize("id, Tarjeta", 
                             [(1000, {'id_tarjeta': 1000, 'fecha_verificada': '02/01/2027', 'nip': 3031, 'intentos': 0, 'saldo': 56000.0, 'limite': 10000.0, 'bloqueada': False, 'verificada': True, 'id_usuario': 75}),
                             (1001, {'id_tarjeta': 1001, 'fecha_verificada': '13/10/2026', 'nip': 7880, 'intentos': 0, 'saldo': 78806.0, 'limite': 10000.0, 'bloqueada': True, 'verificada': True, 'id_usuario': 43}),
                             (1002, {'id_tarjeta': 1002, 'fecha_verificada': '25/10/2025', 'nip': 7032, 'intentos': 0, 'saldo': 70326.0, 'limite': 10000.0, 'bloqueada': False, 'verificada': True, 'id_usuario': 96}),
                             (1003, {'id_tarjeta': 1003, 'fecha_verificada': '08/10/2028', 'nip': 9900, 'intentos': 1, 'saldo': 44912.0, 'limite': 10000.0, 'bloqueada': False, 'verificada': True, 'id_usuario': 10}),
                             (1004, {'id_tarjeta': 1004, 'fecha_verificada': '21/03/2024', 'nip': 4161, 'intentos': 0, 'saldo': 96954.0, 'limite': 10000.0, 'bloqueada': False, 'verificada': True, 'id_usuario': 8})])
    def test_consulta_tarjeta_validas_5_primeras(self,id, Tarjeta):
        """_summary_

        Args:
            id (int): Argumento de entrada
            expected_result (bool): Argumrnto de salida esperado
        """
        assert TarjetaDao.consulta_tarjeta(id) == Tarjeta
        
    @pytest.mark.parametrize("id, expected_result", 
                             [(1044, {'id_tarjeta': 1044, 'fecha_verificada': '04/01/2026', 'nip': 6663, 'intentos': 1, 'saldo': 4681.0, 'limite': 10000.0, 'bloqueada': False, 'verificada': True, 'id_usuario': 37}),
                             (1045, {'id_tarjeta': 1045, 'fecha_verificada': '24/03/2026', 'nip': 8624, 'intentos': 1, 'saldo': 110747.0, 'limite': 10000.0, 'bloqueada': False, 'verificada': True, 'id_usuario': 37}),
                             (1046, {'id_tarjeta': 1046, 'fecha_verificada': '11/11/2030', 'nip': 4800, 'intentos': 3, 'saldo': 126920.0, 'limite': 10000.0, 'bloqueada': True, 'verificada': False, 'id_usuario': 77}),
                             (1047, {'id_tarjeta': 1047, 'fecha_verificada': '04/05/2028', 'nip': 6312, 'intentos': 0, 'saldo': 54803.0, 'limite': 10000.0, 'bloqueada': False, 'verificada': True, 'id_usuario': 29}),
                             (1048, {'id_tarjeta': 1048, 'fecha_verificada': '06/06/2023', 'nip': 2080, 'intentos': 0, 'saldo': 2132.0, 'limite': 10000.0, 'bloqueada': False, 'verificada': True, 'id_usuario': 26}),
                             (1049, {'id_tarjeta': 1049, 'fecha_verificada': '22/01/2029', 'nip': 6106, 'intentos': 0, 'saldo': 3149.0, 'limite': 10000.0, 'bloqueada': False, 'verificada': False, 'id_usuario': 97})])
    def test_consulta_tarjeta_validas_5_ultimas(self,id, expected_result):
        """_summary_

        Args:
            id (int): Argumento de entrada
            expected_result (bool): Argumrnto de salida esperado
        """
        assert TarjetaDao.consulta_tarjeta(id) == expected_result

    #-------------- Pruebas unitarias para valores no validos ------------
    
    @pytest.mark.parametrize("id, expected_result", 
                             [(994, None),
                             (995, None),
                             (996, None),
                             (997, None),
                             (998, None),
                             (999, None)])
    def test_consulta_tarjeta_no_validas_limite_inferior(self,id, expected_result):
        """_summary_

        Args:
            id (int): Argumento de entrada
            expected_result (bool): Argumrnto de salida esperado
        """
        assert TarjetaDao.consulta_tarjeta(id) == expected_result
    
    @pytest.mark.parametrize("id, expected_result", 
                             [(1050, None),
                             (1051, None),
                             (1052, None),
                             (1053, None),
                             (1054, None),
                             (1055, None)])
    def test_consulta_tarjeta_no_validas_limite_exterior(self,id, expected_result):
        """_summary_

        Args:
            id (int): Argumento de entrada
            expected_result (bool): Argumrnto de salida esperado
        """
        assert TarjetaDao.consulta_tarjeta(id) == expected_result
    
    @pytest.mark.parametrize("id, expected_result", 
                             [(10.05, "El tipo de dato debe ser un entero"),
                             ('1051', "El tipo de dato debe ser un entero"),
                             (10.52, "El tipo de dato debe ser un entero"),
                             ('1053', "El tipo de dato debe ser un entero"),
                             ('1054', "El tipo de dato debe ser un entero"),
                             ('1055', "El tipo de dato debe ser un entero")])
    def test_consulta_tarjeta_no_validas_no_tipo(self, id, expected_result):
        
        with pytest.raises(BaseException) as error:
            TarjetaDao.consulta_tarjeta(id)
        assert  str(error.value) == expected_result
        
    """
    ------------------- Pruebas para verifica_tarjeta -----------------------
    """
    # ------------------ Pruebas con valores validos -------------------
    
    @pytest.mark.parametrize("id, expected_result", 
                             [(1000, {'id_tarjeta': 1000, 'fecha_verificada': '02/01/2027', 'nip': None, 'intentos': None, 'saldo': None, 'limite': None, 'bloqueada': None, 'verificada': True, 'id_usuario': None}),
                             (1001, {'id_tarjeta': 1001, 'fecha_verificada': '13/10/2026', 'nip': None, 'intentos': None, 'saldo': None, 'limite': None, 'bloqueada': None, 'verificada': True, 'id_usuario': None}),
                             (1002, {'id_tarjeta': 1002, 'fecha_verificada': '25/10/2025', 'nip': None, 'intentos': None, 'saldo': None, 'limite': None, 'bloqueada': None, 'verificada': True, 'id_usuario': None}),
                             (1003, {'id_tarjeta': 1003, 'fecha_verificada': '08/10/2028', 'nip': None, 'intentos': None, 'saldo': None, 'limite': None, 'bloqueada': None, 'verificada': True, 'id_usuario': None}),
                             (1004, {'id_tarjeta': 1004, 'fecha_verificada': '21/03/2024', 'nip': None, 'intentos': None, 'saldo': None, 'limite': None, 'bloqueada': None, 'verificada': True, 'id_usuario': None})])
    def test_verifica_tarjeta_validas_5_primeras(self,id, expected_result):
        """_summary_

        Args:
            id (int): Argumento de entrada
            expected_result (bool): Argumrnto de salida esperado
        """
        assert TarjetaDao.verifica_tarjeta(id) == expected_result
    
    @pytest.mark.parametrize("id, expected_result", 
                             [(1044, {'id_tarjeta': 1044, 'fecha_verificada': '04/01/2026', 'nip': None, 'intentos': None, 'saldo': None, 'limite': None, 'bloqueada': None, 'verificada': True, 'id_usuario': None}),
                             (1045, {'id_tarjeta': 1045, 'fecha_verificada': '24/03/2026', 'nip': None, 'intentos': None, 'saldo': None, 'limite': None, 'bloqueada': None, 'verificada': True, 'id_usuario': None}),
                             (1046, {'id_tarjeta': 1046, 'fecha_verificada': '11/11/2030', 'nip': None, 'intentos': None, 'saldo': None, 'limite': None, 'bloqueada': None, 'verificada': False, 'id_usuario': None}),
                             (1047,  {'id_tarjeta': 1047, 'fecha_verificada': '04/05/2028', 'nip': None, 'intentos': None, 'saldo': None, 'limite': None, 'bloqueada': None, 'verificada': True, 'id_usuario': None}),
                             (1048, {'id_tarjeta': 1048, 'fecha_verificada': '06/06/2023', 'nip': None, 'intentos': None, 'saldo': None, 'limite': None, 'bloqueada': None, 'verificada': True, 'id_usuario': None})])
    def test_verifica_tarjeta_validas_5_ultimas(self,id, expected_result):
        """_summary_

        Args:
            id (int): Argumento de entrada
            expected_result (bool): Argumrnto de salida esperado
        """
        assert TarjetaDao.verifica_tarjeta(id) == expected_result
        
    
    # -------------Pruebas con valores invalidos --------------------
    
    @pytest.mark.parametrize("id, expected_result", 
                             [(994, None),
                             (995, None),
                             (996, None),
                             (997, None),
                             (998, None),
                             (999, None)])
    def test_verifica_tarjeta_no_validas_limite_inferior(self,id, expected_result):
        """_summary_

        Args:
            id (int): Argumento de entrada
            expected_result (bool): Argumrnto de salida esperado
        """
        assert TarjetaDao.verifica_tarjeta(id) == expected_result
    
    @pytest.mark.parametrize("id, expected_result", 
                             [(1050, None),
                             (1051, None),
                             (1052, None),
                             (1053, None),
                             (1054, None),
                             (1055, None)])
    def test_verifica_tarjeta_no_validas_limite_exterior(self,id, expected_result):
        """_summary_

        Args:
            id (int): Argumento de entrada
            expected_result (bool): Argumrnto de salida esperado
        """
        assert TarjetaDao.verifica_tarjeta(id) == expected_result

    @pytest.mark.parametrize("id, expected_result", 
                             [(10.001, "El tipo de dato debe ser un entero"),
                             (-10.005, "El tipo de dato debe ser un entero"),
                             ('1052', "El tipo de dato debe ser un entero"),
                             ('1053', "El tipo de dato debe ser un entero"),
                             ('A', "El tipo de dato debe ser un entero"),
                             ('1055', "El tipo de dato debe ser un entero")])
    def test_verifica_tarjeta_no_validas_no_tipo(self, id, expected_result):
        
        with pytest.raises(BaseException) as error:
            TarjetaDao.verifica_tarjeta(id)
        assert  str(error.value) == expected_result
        
    """
    -------------------- Pruebas unitarias para verifica_fecha ------------------------
    """
    
    @pytest.mark.parametrize("id, expected_result", 
                             [(1000, True),
                             (1001, True),
                             (1002, True),
                             (1003, True),
                             (1004, False),
                             (1005, True)])
    def test_fecha_verificada_validas_5_primeras(self,id, expected_result):
        """_summary_

        Args:
            id (int): Argumento de entrada
            expected_result (bool): Argumrnto de salida esperado
        """
        assert TarjetaDao.verifica_fecha(id) == expected_result
    
    @pytest.mark.parametrize("id, expected_result", 
                             [(1044, True),
                             (1045, True),
                             (1046, True),
                             (1047, True),
                             (1048, False),
                             (1049, True)])
    def test_fecha_verificada_validas_5_ultimas(self,id, expected_result):
        """_summary_

        Args:
            id (int): Argumento de entrada
            expected_result (bool): Argumrnto de salida esperado
        """
        assert TarjetaDao.verifica_fecha(id) == expected_result
    
    @pytest.mark.parametrize("id, expected_result", 
                             [(10.001, "El tipo de dato debe ser un entero"),
                             (-10.005, "El tipo de dato debe ser un entero"),
                             ('1052', "El tipo de dato debe ser un entero"),
                             ('1053', "El tipo de dato debe ser un entero"),
                             ('A', "El tipo de dato debe ser un entero"),
                             ('1055', "El tipo de dato debe ser un entero")])
    def test_fecha_verificada_no_validas_no_tipo(self, id, expected_result):
        
        with pytest.raises(BaseException) as error:
            TarjetaDao.verifica_fecha(id)
        assert  str(error.value) == expected_result
    
    """
    ---------------- Pruebas para verifica_bloqueo ------------------
    """
    #------------- Pruebas unitaria para parametros validos ---------
    
    @pytest.mark.parametrize("id, expected_result", 
                             [(1000, {'id_tarjeta': 1000, 'fecha_verificada': '02/01/2027', 'nip': None, 'intentos': None, 'saldo': None, 'limite': None, 'bloqueada': False, 'verificada': None, 'id_usuario': None}),
                             (1001, {'id_tarjeta': 1001, 'fecha_verificada': '13/10/2026', 'nip': None, 'intentos': None, 'saldo': None, 'limite': None, 'bloqueada': True, 'verificada': None, 'id_usuario': None}),
                             (1002, {'id_tarjeta': 1002, 'fecha_verificada': '25/10/2025', 'nip': None, 'intentos': None, 'saldo': None, 'limite': None, 'bloqueada': False, 'verificada': None, 'id_usuario': None}),
                             (1003, {'id_tarjeta': 1003, 'fecha_verificada': '08/10/2028', 'nip': None, 'intentos': None, 'saldo': None, 'limite': None, 'bloqueada': False, 'verificada': None, 'id_usuario': None}),
                             (1004, {'id_tarjeta': 1004, 'fecha_verificada': '21/03/2024', 'nip': None, 'intentos': None, 'saldo': None, 'limite': None, 'bloqueada': False, 'verificada': None, 'id_usuario': None})])
    def test_verifica_bloqueo_validas_5_primeras(self, id, expected_result):
        """_summary_

        Args:
            id (int): Argumento de entrada
            expected_result (bool): Argumrnto de salida esperado
        """
        assert TarjetaDao.verifica_bloqueo(id) == expected_result
    
    @pytest.mark.parametrize("id, expected_result", 
                             [(1045, {'id_tarjeta': 1045, 'fecha_verificada': '24/03/2026', 'nip': None, 'intentos': None, 'saldo': None, 'limite': None, 'bloqueada': False, 'verificada': None, 'id_usuario': None}),
                             (1046, {'id_tarjeta': 1046, 'fecha_verificada': '11/11/2030', 'nip': None, 'intentos': None, 'saldo': None, 'limite': None, 'bloqueada': True, 'verificada': None, 'id_usuario': None}),
                             (1047, {'id_tarjeta': 1047, 'fecha_verificada': '04/05/2028', 'nip': None, 'intentos': None, 'saldo': None, 'limite': None, 'bloqueada': False, 'verificada': None, 'id_usuario': None}),
                             (1048,  {'id_tarjeta': 1048, 'fecha_verificada': '06/06/2023', 'nip': None, 'intentos': None, 'saldo': None, 'limite': None, 'bloqueada': False, 'verificada': None, 'id_usuario': None}),
                             (1049, {'id_tarjeta': 1049, 'fecha_verificada': '22/01/2029', 'nip': None, 'intentos': None, 'saldo': None, 'limite': None, 'bloqueada': False, 'verificada': None, 'id_usuario': None})])
    def test_verifica_bloqueo_validas_5_ultimas(self, id, expected_result):
        """_summary_

        Args:
            id (int): Argumento de entrada
            expected_result (bool): Argumrnto de salida esperado
        """
        assert TarjetaDao.verifica_bloqueo(id) == expected_result
        
    #-------------- Pruebas unitarias para valores no validos ------------
    
    @pytest.mark.parametrize("id, expected_result", 
                             [(994, None),
                             (995, None),
                             (996, None),
                             (997, None),
                             (998, None),
                             (999, None)])
    def test_verifica_bloqueo_no_validas_limite_inferior(self,id, expected_result):
        """_summary_

        Args:
            id (int): Argumento de entrada
            expected_result (bool): Argumrnto de salida esperado
        """
        assert TarjetaDao.verifica_bloqueo(id) == expected_result
    
    @pytest.mark.parametrize("id, expected_result", 
                             [(1050, None),
                             (1051, None),
                             (1052, None),
                             (1053, None),
                             (1054, None),
                             (1055, None)])
    def test_verifica_bloqueo_no_validas_limite_exterior(self,id, expected_result):
        """_summary_

        Args:
            id (int): Argumento de entrada
            expected_result (bool): Argumrnto de salida esperado
        """
        assert TarjetaDao.verifica_bloqueo(id) == expected_result
    
    @pytest.mark.parametrize("id, expected_result", 
                             [(10.001, "El tipo de dato debe ser un entero"),
                             (-10.005, "El tipo de dato debe ser un entero"),
                             ('1052', "El tipo de dato debe ser un entero"),
                             ('1053', "El tipo de dato debe ser un entero"),
                             ('A', "El tipo de dato debe ser un entero"),
                             ('1055', "El tipo de dato debe ser un entero")])
    def test_verifica_bloqueo_no_validas_no_tipo(self, id, expected_result):
        
        with pytest.raises(BaseException) as error:
            TarjetaDao.verifica_bloqueo(id)
        assert  str(error.value) == expected_result
    
    """ -------------------------- Verifica NIP -------------------------------"""
    
    #------------- Pruebas unitaria para parametros validos ---------   
    
    @pytest.mark.parametrize("id, nip, expected_status, excpect_affected", 
                             [(1000, 3031, True, 1),
                             (1001, 7880, True, 1),
                             (1002, 7032, True, 1),])
    def test_verifica_nip_valores_validos(self, id, nip, expected_status, excpect_affected):
        row_nip, row_affected = TarjetaDao.verifica_nip(id, nip)
        assert row_nip == expected_status and row_affected == excpect_affected
    
    #------------------- Pruebas unitarias para parametros invalidos-----------
    
    @pytest.mark.parametrize("id, nip, expected_status, excpect_affected", 
                             [(1005, 3031, False, 1),
                             (1007, 7880, False, 1),
                             (1029, 7032, False, 1),])
    def test_verifica_nip_valores_no_validos(self, id, nip, expected_status, excpect_affected):
        row_nip, row_affected = TarjetaDao.verifica_nip(id, nip)
        assert row_nip == expected_status and row_affected == excpect_affected
    
    
    
    
    
    