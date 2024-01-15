<?php

namespace App\Admin\Controllers;

use App\Admin\Repositories\Inspector;
use App\Models\Department;
use Dcat\Admin\Form;
use Dcat\Admin\Grid;
use Dcat\Admin\Show;
use Dcat\Admin\Http\Controllers\AdminController;

class InspectorController extends AdminController
{
    /**
     * Make a grid builder.
     *
     * @return Grid
     */
    protected function grid()
    {
        return Grid::make(new Inspector("department"), function (Grid $grid) {
            $grid->column('id')->sortable();
            $grid->column('name');
            $grid->column('department.name', "部门");
            $grid->column('phone');
            $grid->column('created_at');
            $grid->column('updated_at')->sortable();

            $grid->filter(function (Grid\Filter $filter) {
                $filter->equal('id');

            });
        });
    }

    /**
     * Make a show builder.
     *
     * @param mixed $id
     *
     * @return Show
     */
    protected function detail($id)
    {
        return Show::make($id, new Inspector("department"), function (Show $show) {
            $show->field('id');
            $show->field('name');
            $show->field('department.name', '部门');
            $show->field('phone');
            $show->field('created_at');
            $show->field('updated_at');
        });
    }

    /**
     * Make a form builder.
     *
     * @return Form
     */
    protected function form()
    {
        return Form::make(new Inspector(), function (Form $form) {
            $form->display('id');
            $form->text('name')->required();
            $departments = Department::all();
            $dep = [];
            for ($i = 0; $i < count($departments); $i++){
                $dep[$departments[$i]->id] = $departments[$i]->name;
            }
            $form->select('department_id')->options($dep)->required();
            $form->text('phone')->required()->type('number')->minLength(11)->maxLength(11);

//            $form->display('created_at');
//            $form->display('updated_at');
        });
    }
}
