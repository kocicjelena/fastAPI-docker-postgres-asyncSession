import UpdateTodo from './UpdateTodo'
import DeleteTodo from './DeleteTodo'

function RenderTodo({item, id, fetchTodos}) {
    return (
      <div className="col mb-5">
      <div className="card" style={{width: "18rem"}}>
              <UpdateTodo item={item} id={id} fetchTodos={fetchTodos}/>
              <DeleteTodo id={id} fetchTodos={fetchTodos}/>  {/* new */}
            </div>
            </div>
    )
  }
  export default RenderTodo;