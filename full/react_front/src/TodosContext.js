import React, { useEffect, useState } from "react";
const TodosContext = React.createContext({
    todos: [], fetchTodos: () => {}
  })
export default TodosContext;