package utn.estudiantes.servicio;

import utn.estudiante.modelo.Estudiante;

import java.util.List;

public interface iEstudianteServicio {
    public List<Estudiante> listarEstudiantes();
    public Estudiante buscarEstudianteporId(Integer idEstudiante);
    public void guardarEstudiante(Estudiante estudiante);
    public void eliminarEstudiante(Estudiante estudiante);
}