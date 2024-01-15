<?php

namespace App\Admin\Controllers;

use App\Admin\Repositories\Project;
use Dcat\Admin\Form;
use Dcat\Admin\Grid;
use Dcat\Admin\Show;
use Dcat\Admin\Http\Controllers\AdminController;

class ProjectController extends AdminController
{
    /**
     * Make a grid builder.
     *
     * @return Grid
     */
    protected function grid()
    {
        return Grid::make(new Project(), function (Grid $grid) {
            $grid->column('id')->sortable();
            $grid->column('name');
            $grid->column('place_id');
            $grid->column('options');
            $grid->column('photo');
            $grid->column('video');
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
        return Show::make($id, new Project(), function (Show $show) {
            $show->field('id');
            $show->field('name');
            $show->field('place_id');
            $show->field('options');
            $show->field('photo');
            $show->field('video');
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
        return Form::make(new Project(), function (Form $form) {
            $form->display('id');
            $form->text('name');
            $form->text('place_id');
            $form->text('options');
            $form->text('photo');
            $form->text('video');

            $form->display('created_at');
            $form->display('updated_at');
        });
    }
}
