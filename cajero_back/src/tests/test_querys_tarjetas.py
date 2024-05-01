import pytest
from dao.TarjetaDAO import TarjetaDao
import datetime
from decimal import Decimal
from exceptions.TipoDatoException import TipoDatoException
class TestQuerysTarjeta:
    
    #------------- Preubas unitarias de limites ---------------------
    """
    ---------------- Pruebas para consulta_tarjeta ------------------
    """
    #------------- Pruebas unitaria para parametros validos ---------
    
    @pytest.mark.parametrize("id, Tarjeta", 
                             [(1000, (1000, datetime.date(2027, 1, 2), 3031, 0, Decimal('48578.00'), Decimal('10000.00'), False, True, 75)),
                             (1001, (1001, datetime.date(2026, 10, 13), 7880, 0, Decimal('78806.00'), Decimal('10000.00'), False, True, 43)),
                             (1002, (1002, datetime.date(2025, 10, 25), 7032, 0, Decimal('70326.00'), Decimal('10000.00'), False, True, 96)),
                             (1003, (1003, datetime.date(2028, 10, 8), 9900, 1, Decimal('44912.00'), Decimal('10000.00'), False, True, 10)),
                             (1004, (1004, datetime.date(2024, 3, 21), 4161, 0, Decimal('96954.00'), Decimal('10000.00'), False, True, 8))])
    def test_consulta_tarjeta_validas_5_primeras(self,id, Tarjeta):
        """_summary_

        Args:
            id (int): Argumento de entrada
            expected_result (bool): Argumrnto de salida esperado
        """
        assert TarjetaDao.consulta_tarjeta(id) == Tarjeta
        
    @pytest.mark.parametrize("id, expected_result", 
                             [(1044, (1044, datetime.date(2026, 1, 4), 6663, 1, Decimal('4681.00'), Decimal('10000.00'), False, True, 37)),
                             (1045, (1045, datetime.date(2026, 3, 24), 8624, 1, Decimal('110747.00'), Decimal('10000.00'), False, True, 37)),
                             (1046, (1046, datetime.date(2030, 11, 11), 4800, 3, Decimal('126920.00'), Decimal('10000.00'), True, False, 77)),
                             (1047, (1047, datetime.date(2028, 5, 4), 6312, 0, Decimal('54803.00'), Decimal('10000.00'), False, True, 29)),
                             (1048, (1048, datetime.date(2023, 6, 6), 2080, 0, Decimal('2132.00'), Decimal('10000.00'), False, True, 26)),
                             (1049, (1049, datetime.date(2029, 1, 22), 6106, 0, Decimal('3149.00'), Decimal('10000.00'), False, False, 97))])
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
                             [(1000, (True,)),
                             (1001, (True,)),
                             (1002, (True,)),
                             (1003, (True,)),
                             (1004, (True,)),
                             (1005, (True,))])
    def test_verifica_tarjeta_validas_5_primeras(self,id, expected_result):
        """_summary_

        Args:
            id (int): Argumento de entrada
            expected_result (bool): Argumrnto de salida esperado
        """
        assert TarjetaDao.verifica_tarjeta(id) == expected_result
    
    @pytest.mark.parametrize("id, expected_result", 
                             [(1044, (True,)),
                             (1045, (True,)),
                             (1046, (False,)),
                             (1047, (True,)),
                             (1048, (True,)),
                             (1049, (False,))])
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
                             [(1000, (False,)),
                             (1001, (False,)),
                             (1002, (False,)),
                             (1003, (False,)),
                             (1004, (False,)),
                             (1005, (True,))])
    def test_verifica_bloqueo_validas_5_primeras(self, id, expected_result):
        """_summary_

        Args:
            id (int): Argumento de entrada
            expected_result (bool): Argumrnto de salida esperado
        """
        assert TarjetaDao.verifica_bloqueo(id) == expected_result
    
    @pytest.mark.parametrize("id, expected_result", 
                             [(1044, (False,)),
                             (1045, (False,)),
                             (1046, (True,) ),
                             (1047, (False,)),
                             (1048, (False,)),
                             (1049, (False,))])
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
                             [(1000, 3031, False, 1),
                             (1001, 7880, False, 1),
                             (1002, 7032, False, 1),])
    def test_verifica_nip_valores_validos(self, id, nip, expected_status, excpect_affected):
        row_nip, row_affected = TarjetaDao.verifica_nip(id, nip)
        assert row_nip == expected_status and row_affected == excpect_affected
    
    #------------------- Pruebas unitarias para parametros invalidos-----------
    
    @pytest.mark.parametrize("id, nip, expected_status, excpect_affected", 
                             [(1005, 3031, True, 1),
                             (1007, 7880, True, 1),
                             (1029, 7032, True, 1),])
    def test_verifica_nip_valores_validos(self, id, nip, expected_status, excpect_affected):
        row_nip, row_affected = TarjetaDao.verifica_nip(id, nip)
        assert row_nip == expected_status and row_affected == excpect_affected
    
    
    
    
    
    