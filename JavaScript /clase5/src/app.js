import morgan from "morgan";
import express from "express";
import tareasRoutes from "./router/tareas.routes.js"
import authRoutes from "./router/auth.routes.js"

const app = express();
//Middlewares
app.use(morgan("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: false}));

app.get("/", (req, res) => res.json({ message: "Bienvenidos a mi proyecto"}));
app.use('/api',tareasRoutes);
app.use('/api',authRoutes);

//Manejando errores
app.use((err, req, res, next) => {
    res.status(500).json({
        status: "error",
        message: err.message
    })
});

export default app;