from schemas import TipoDeInformacion, NivelDeInformacion, EstadoAvanceInformacion
from typing import List

# TODO: Mejorar y completar

class NivelDeInformacionRepository:
    ndis = []

    def create_ndi(self, ndi: NivelDeInformacion) -> NivelDeInformacion:
        pass

    def get_ndi_by_code(self, ndi_code: NivelDeInformacion.code) -> List[NivelDeInformacion]:
        pass

    def get_all_ndis(self) -> List[NivelDeInformacion]:
        pass


class TipoDeInformacionRepository:
    tdis = []

    def create_tdi(self, tdi: TipoDeInformacion) -> TipoDeInformacion:
        pass

    def get_tdi_by_code(self, tdi_code: TipoDeInformacion.code) -> List[TipoDeInformacion]:
        pass

    def get_all_tdis(self) -> List[TipoDeInformacion]:
        pass


class EstadoAvanceInformacionRepository:
    eaims = []

    def create_tdi(self, eaim: EstadoAvanceInformacion) -> EstadoAvanceInformacion:
        pass

    def get_eaim_by_code(self, eaim_code: EstadoAvanceInformacion.code) -> List[EstadoAvanceInformacion]:
        pass

    def get_all_eaims(self) -> List[EstadoAvanceInformacion]:
        pass