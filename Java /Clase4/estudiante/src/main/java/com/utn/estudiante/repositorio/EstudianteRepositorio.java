package com.utn.estudiante.repositorio;

import org.springframework.data.jpa.repository.JpaRepository;
import com.utn.estudiante.modelo.Estudiante;

public interface EstudianteRepositorio extends JpaRepository<Estudiante, Integer> {
}