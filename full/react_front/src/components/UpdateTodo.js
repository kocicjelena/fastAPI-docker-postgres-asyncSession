import React, { useEffect, useState } from "react";
import TodosContext from '../TodosContext'
function UpdateTodo({item, id}) {
  
    const [todo, setTodo] = useState(item)
    const {fetchTodos} = React.useContext(TodosContext)
  
    const updateTodo = async () => {
      await fetch(`http://localhost:8000/todo/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ item: todo })
      })
      
      await fetchTodos()
    }
  
    return (
      <>
        {/* <button h="1.5rem" size="sm">Update Todo</button> */}
        <div className="mb-3">
            <input
            pr="4.5rem"
                  type="text"
                  placeholder="Add a todo item"
                  aria-label="Add a todo item"
                  value={todo}
                  onChange={e => setTodo(e.target.value)}
                />
          
            </div>
  
            <div className="mb-3">
              <button h="1.5rem" size="sm" onClick={updateTodo}>Update Todo</button>
            </div>
      
      </>
    )
  }
  export default UpdateTodo;