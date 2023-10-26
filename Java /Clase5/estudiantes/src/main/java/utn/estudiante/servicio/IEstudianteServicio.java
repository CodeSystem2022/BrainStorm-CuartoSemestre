package utn.estudiantes.servicio;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import utn.estudiantes.modelo.Estudiantes2022;

import java.util.List;

public interface IEstudianteServicio {
    public List<Estudiantes2022> listarEstudiantes();
    public Estudiantes2022 buscarEstudiantePorId(Integer idEstudiantes2022);
    public void guardarEstudiante(Estudiantes2022 estudiante);
    public void eliminarEstudiante(Estudiantes2022 estudiante);

}