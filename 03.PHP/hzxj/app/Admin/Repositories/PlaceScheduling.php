<?php

namespace App\Admin\Repositories;

use App\Models\PlaceScheduling as Model;
use Dcat\Admin\Repositories\EloquentRepository;

class PlaceScheduling extends EloquentRepository
{
    /**
     * Model.
     *
     * @var string
     */
    protected $eloquentClass = Model::class;
}
